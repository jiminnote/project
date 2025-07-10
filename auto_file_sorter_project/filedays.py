# 파일별 수정일을 기준으로 정리

import os
import shutil
from datetime import datetime

from project.filetidy_project.collect_png_images import collect_screenshots


def get_file_date(path):
    t = os.path.getmtime(path)
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d')

def move_files_date(src_path, dest_path):
    for file in os.listdir(src_path):
        file_path = os.path.join(src_path, file)
        if os.path.isdir(file_path):
            try:
                mod_date = get_file_date(file_path)
                dest_folder = os.path.join(dest_path, mod_date)

                ext = file.split(".")[-1]
                ext_folder = os.path.join(dest_folder, ext)
                os.makedirs(ext_folder, exist_ok=True)

                shutil.move(file_path, os.path.join(ext_folder, file))
                print(f"{file}->{mod_date}/{ext}/")
            except Exception as e:
                print(e)

def main() :
    src = '/Users/jimin/Desktop'
    dest = './screenshots'

    collect_screenshots(src, dest)
    print("SUCCESS!!")

    if not os.path.exists(src):
        print("No Exist!!")
        return

    move_files_date(src, dest)
    print("SUCCESS!!")
if __name__ == "__main__":
    main()
