import os
import shutil

path = "C:/Users/Downloads"

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    ext = ext[1:]

    if ext:
        folder = os.path.join(path, ext)
        if not os.path.exists(folder):
            os.makedirs(folder)
        shutil.move(os.path.join(path, file), folder)
