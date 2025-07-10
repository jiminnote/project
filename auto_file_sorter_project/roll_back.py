import os
import shutil

def rollback_files(organized_root, restore_path):
    for date_folder in os.listdir(organized_root):
        date_path = os.path.join(organized_root, date_folder)
        if os.path.isdir(date_path):
            for ext_folder in os.listdir(date_path):
                ext_path = os.path.join(date_path, ext_folder)
                if os.path.isdir(ext_path):
                    for file in os.listdir(ext_path):
                        src_file = os.path.join(ext_path, file)
                        dst_file = os.path.join(restore_path, file)

                        try:
                            shutil.move(src_file, dst_file)
                            print(f"복구: {file} → downloads/")
                        except Exception as e:
                            print(f"복구 실패: {file} | {e}")

def main():
    # organized_root = './organized_files'  # 이동된 곳
    # restore_path = '/Users/jimin/downloads'  # 되돌릴 곳
    organized_root = './screenshots'
    restore_path = '/Users/jimin/Desktop'

    if not os.path.exists(restore_path):
        os.makedirs(restore_path)

    rollback_files(organized_root, restore_path)
    print("✅ 롤백 완료!")

if __name__ == "__main__":
    main()