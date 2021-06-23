from pathlib import Path

p = Path('C:\\Users\\user\\Desktop\\Old')
def parse_folder(path):
    files = []
    folders = []
    folders = [x.name for x in p.iterdir() if x.is_dir()]
    files = [e.name for e in p.iterdir() if e.is_dir()]


    print(files, folders)
    return files, folders

parse_folder(p)