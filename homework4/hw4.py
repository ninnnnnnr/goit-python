from pathlib import Path
import sys

p = Path(sys.argv[1])

image_types = 'jpeg', 'png', 'jpg', 'svg'
image = []
video_types = 'avi', 'mp4', 'mov', 'mkv'
video = []
document_types = 'doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'
document = []
music_types = 'mp3', 'ogg', 'wav', 'amr'
music = []
zip_types = 'zip', 'gz', 'tar', 'rar'
zip_file = []
other = []


def parse_folder(path):
    global image_types, image, video_types, video, document_types, document, music_types, music, zip_types, zip_file, other
    for el in path.iterdir():
        if el.is_file():
            if el.name.endswith(image_types):
                image.append(el.name)
            elif el.name.endswith(document_types):
                document.append(el.name)
            elif el.name.endswith(video_types):
                video.append(el.name)
            elif el.name.endswith(music_types):
                music.append(el.name)
            elif el.name.endswith(zip_types):
                zip_file.append(el.name)
            else:
                other.append(el.name)

    print(f"Files image:{image}")
    print(f"Files video:{video}")
    print(f"Files document:{document}")
    print(f"Files music:{music}")
    print(f"Files zip:{zip_file}")
    print(f"Files other:{other}")



def parse_folder_recursion(path):
    global image_types, image, video_types, video, document_types, document, music_types, music, zip_types, zip_file, other
    for element in path.iterdir():
        if element.is_dir():
            parse_folder_recursion(element)
        else:
            if element.name.endswith(image_types):
                image.append(element.name)
            elif element.name.endswith(document_types):
                document.append(element.name)
            elif element.name.endswith(video_types):
                video.append(element.name)
            elif element.name.endswith(music_types):
                music.append(element.name)
            elif element.name.endswith(zip_types):
                zip_file.append(element.name)
            else:
                other.append(element.name)

        print(f"Files image:{image}")
        print(f"Files video:{video}")
        print(f"Files document:{document}")
        print(f"Files music:{music}")
        print(f"Files zip:{zip_file}")
        print(f"Files other:{other}")


print(parse_folder_recursion(p))

# python hw4.py C:\Users\user\Desktop\Old