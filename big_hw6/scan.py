import sys
from pathlib import Path

#p = Path('C:\goit\goit-python\Module6\\big_hw\Old')

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

