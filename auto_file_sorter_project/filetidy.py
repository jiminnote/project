import os.path
import shutil
from datetime import datetime

def create_date_folder(base_path):
    today = datetime.today().strftime("%Y-%m-%d")
    folder_path = os.path.join(base_path, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def get_file_list(src_path):
    return [ f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, f))]

def move_files_extension(src_path, dest_path):
    files = get_file_list(src_path)
    for file in files:
        try:
            ext = file.split(".")[-1]
            ext_folder = os.path.join(dest_path, file)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(src_path, file), os.path.join(ext_folder, file))
            print(f"{file}->{ext}/")
        except Exception as e:
            print(e)

def main():
    src = '/Users/jimin/downloads'
    base = './organized_files'

    if not os.path.exists(src):
        print("No exists folder!!")
        return

    today_folder = create_date_folder(base)
    move_files_extension(src, today_folder)
    print("SUCCESS!!")

if __name__ == "__main__":
    main()

