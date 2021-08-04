import sys
from pathlib import Path
import re
import sys
from pathlib import Path
import shutil
import scan
from normalize import normalize


# scan code start
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()
AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIOS = []
OGG_AUDIOS = []
WAV_AUDIOS = []
AMR_AUDIOS = []
ZIP_ARCH = []
GZ_ARCH = []
TAR_ARCH = []

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "AVI": AVI_VIDEOS,
    "MP4": MP4_VIDEOS,
    "MOV": MOV_VIDEOS,
    "MKV": MKV_VIDEOS,
    "DOC": DOC_DOCUMENTS,
    "DOCX": DOCX_DOCUMENTS,
    "TXT": TXT_DOCUMENTS,
    "PDF": PDF_DOCUMENTS,
    "XLSX": XLSX_DOCUMENTS,
    "PPTX": PPTX_DOCUMENTS,
    "MP3": MP3_AUDIOS,
    "OGG": OGG_AUDIOS,
    "WAV": WAV_AUDIOS,
    "AMR": AMR_AUDIOS,
    "ZIP": ZIP_ARCH,
    "GZ": GZ_ARCH,
    "TAR": TAR_ARCH
}


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "JPG", "PNG", "SVG", "AVI", "MP4", "MOV", "MKV",
                                 "DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX", "MP3", "OGG",
                                 "WAV", "AMR", "ZIP", "GZ", "TAR", "OTHER"):
                FOLDERS.append(item)
                scan(item)
            continue

        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


if __name__ == "__main__":
    scan_path = sys.argv[0]
    print(f"Start in folder {scan_path}")

    search_folder = Path(scan_path)
    scan(search_folder)
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Videos avi: {AVI_VIDEOS}")
    print(f"Videos mp4: {MP4_VIDEOS}")
    print(f"Videos mov: {MOV_VIDEOS}")
    print(f"Videos mkv: {MKV_VIDEOS}")
    print(f"Documents doc: {DOC_DOCUMENTS}")
    print(f"Documents docx: {DOCX_DOCUMENTS}")
    print(f"Documents txt: {TXT_DOCUMENTS}")
    print(f"Documents pdf: {PDF_DOCUMENTS}")
    print(f"Documents xlsx: {XLSX_DOCUMENTS}")
    print(f"Documents pptx: {PPTX_DOCUMENTS}")
    print(f"Audios mp3: {MP3_AUDIOS}")
    print(f"Audios ogg: {OGG_AUDIOS}")
    print(f"Audios wav: {WAV_AUDIOS}")
    print(f"Audios amr: {AMR_AUDIOS}")
    print(f"Archives zip: {ZIP_ARCH}")
    print(f"Archives gz: {GZ_ARCH}")
    print(f"Archives tar: {TAR_ARCH}")
    print(f"Unknown files: {OTHER}")
    print(f"There are file of types: {EXTENSION}")
    print(f"Unknown types of file: {UNKNOWN}")

    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())

# scan code stop
# normalize code start


CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "e", "u", "ja")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str) -> str:
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name


# normalize code stop
# sort code start


def handle_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_other(file, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def handle_archive(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)  # create folder ARCH
    ext = Path(file).suffix
    folder_for_arch = normalize(file.name.replace(ext, ""))
    archive_folder = target_folder / folder_for_arch
    archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
    try:
        shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()  # Если не успешно удаляем папку под  архив
        return
    file.unlink()  # Если успешно удаляем архив


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")


def handle_formats(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, "")) + ext
    file.replace(target_folder / new_name)


def main(folder):
    scan.scan(folder)

    for file in scan.JPEG_IMAGES:
        handle_image(file, folder, "JPEG")

    for file in scan.JPG_IMAGES:
        handle_image(file, folder, "JPG")

    for file in scan.PNG_IMAGES:
        handle_image(file, folder, "PNG")

    for file in scan.SVG_IMAGES:
        handle_image(file, folder, "SVG")

    for file in scan.OTHER:
        handle_other(file, folder, "OTHER")

    #for file in scan.ARCH:
        #handle_archive(file, folder, "ARCH")

    for file in scan.TAR_ARCH:
        handle_archive(file, folder, "TAR")

    for file in scan.GZ_ARCH:
        handle_archive(file, folder, "GZ")

    for file in scan.ZIP_ARCH:
        handle_archive(file, folder, "ZIP")

    for file in scan.AVI_VIDEOS:
        handle_formats(file, folder, "AVI")

    for file in scan.MP4_VIDEOS:
        handle_formats(file, folder, "MP4")

    for file in scan.MOV_VIDEOS:
        handle_formats(file, folder, "MOV")

    for file in scan.MKV_VIDEOS:
        handle_formats(file, folder, "MKV")

    for file in scan.DOC_DOCUMENTS:
        handle_formats(file, folder, "DOC")

    for file in scan.DOCX_DOCUMENTS:
        handle_formats(file, folder, "DOCX")

    for file in scan.TXT_DOCUMENTS:
        handle_formats(file, folder, "TXT")

    for file in scan.PDF_DOCUMENTS:
        handle_formats(file, folder, "PDF")

    for file in scan.XLSX_DOCUMENTS:
        handle_formats(file, folder, "XLSX")

    for file in scan.PPTX_DOCUMENTS:
        handle_formats(file, folder, "PPTX")

    for file in scan.MP3_AUDIOS:
        handle_formats(file, folder, "MP3")

    for file in scan.OGG_AUDIOS:
        handle_formats(file, folder, "OGG")

    for file in scan.WAV_AUDIOS:
        handle_formats(file, folder, "WAV")

    for file in scan.AMR_AUDIOS:
        handle_formats(file, folder, "AMR")

    for f in scan.FOLDERS:
        handle_folder(f)


if __name__ == "__main__":
    scan_path = sys.argv[0]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())
    main(sort_folder.resolve())


# sort code stop