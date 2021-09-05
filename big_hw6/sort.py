import sys
from pathlib import Path
import shutil
import scan
from normalize import normalize

#p = Path('C:\goit\goit-python\Module6\\big_hw\Old')


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
