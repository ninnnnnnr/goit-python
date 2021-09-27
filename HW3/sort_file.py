from pathlib import Path
import re
import shutil


IMAGES = []
AUDIO = []
VIDEO = []
DOCUMENTS = []
OTHER = []
FOLDERS = []
ARCHIVES = []
UNKNOW = set()
EXTENSIONS = set()

REGISTERED_EXTENSIONS = {
    'JPEG': IMAGES,
    'PNG': IMAGES,
    'JPG': IMAGES,
    'SVG': IMAGES,
    'AVI': VIDEO,
    'MP4': VIDEO,
    'MOV': VIDEO,
    'MKV': VIDEO,
    'DOC': DOCUMENTS,
    'DOCX': DOCUMENTS,
    'TXT': DOCUMENTS,
    'PDF': DOCUMENTS,
    'XLSX': DOCUMENTS,
    'PPTX': DOCUMENTS,
    'MP3': AUDIO,
    'OGG': AUDIO,
    'WAV': AUDIO,
    'AMR': AUDIO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}


def get_extensions(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('Images', 'Audio', 'Video', 'Documents', 'Archives'):
                FOLDERS.append(item)
                scan(item)
            continue
        extension = get_extensions(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSIONS.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOW.add(extension)
                OTHER.append(new_name)


table = {ord('а'): 'a', ord('б'): 'b', ord(
    'в'): 'v', ord('г'): 'h', ord('ґ'): 'g',
    ord('д'): 'd', ord('е'): 'e', ord('є'): 'ie',
    ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'y',
    ord('і'): 'i', ord('ї'): 'i', ord('й'): 'i',
    ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
    ord('н'): 'n', ord('о'): 'o', ord('п'): 'p',
    ord('р'): 'r', ord('с'): 's', ord('т'): 't',
    ord('у'): 'u', ord('ф'): 'f', ord('х'): 'kh',
    ord('ц'): 'ts', ord('ч'): 'ch', ord('ш'): 'sh',
    ord('щ'): 'shch', ord('ю'): 'iu', ord('я'): 'ia',
    ord('А'): 'A', ord('Б'): 'B', ord(
    'В'): 'V', ord('Г'): 'H', ord('Ґ'): 'G',
    ord('Д'): 'D', ord('Е'): 'E', ord('Є'): 'Ye',
    ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'Y',
    ord('І'): 'I', ord('Ї'): 'Yi', ord('Й'): 'Y',
    ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
    ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P',
    ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T',
    ord('У'): 'U', ord('Ф'): 'F', ord('Х'): 'Kh',
    ord('Ц'): 'Ts', ord('Ч'): 'Ch', ord('Ш'): 'Sh',
    ord('Щ'): 'Shch', ord('Ю'): 'Yu', ord('Я'): 'Ya',
    ord('ь'): '', ord('’'): ''}


def normalize(text):

    text = text.translate(table)
    clean_text = re.sub(r'[^\w\s]', '_', text)
    text = clean_text
    return text


def moov_image(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_audio(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_video(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_documents(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_other(file: Path, root_folder: Path, dist: str):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, '')) + ext
    file.replace(target_folder / new_name)


def moov_archive(file, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    new_name = normalize(file.name.replace(ext, ''))
    archive_folder = target_folder / new_name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(file.resolve()),
                              str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        return
    file.unlink()


def deleate_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        pass


def main(folder):
    folder = Path(folder)
    scan(folder)

    for file in IMAGES:
        moov_image(file, folder, 'Images')

    for file in AUDIO:
        moov_audio(file, folder, 'Audio')

    for file in VIDEO:
        moov_video(file, folder, 'Video')

    for file in DOCUMENTS:
        moov_documents(file, folder, 'Documents')

    for file in OTHER:
        moov_other(file, folder, 'Other')

    for file in ARCHIVES:
        moov_archive(file, folder, 'Archives')

    for f in FOLDERS:
        deleate_folder(f)


if __name__ == '__main__':

    input_arg = input('Enter the directory for sorting ')
    sort_folder = Path(input_arg)

    main(sort_folder)