# 이미지 파일들을 모두 정해진 경로에 넣기

import os
import shutil

def collect_png(src_path, dest_path):
    print(f"📁 소스 폴더: {src_path}")
    print(f"📁 목적지 폴더: {dest_path}")

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    files = os.listdir(src_path)
    print(f"📄 전체 파일 개수: {len(files)}")

    png_files = []

    for f in files:
        file_path = os.path.join(src_path, f)
        if os.path.isfile(file_path) and  f.lower().endswith('.png') or f.lower().endswith('.jpg') or f.lower().endswith('.jpeg') :
            png_files.append(f)

    print(f"🖼️ 찾은 PNG 파일 수: {len(png_files)}")

    if not png_files:
        print("❗PNG 파일이 없어요.")
        return

    for file in png_files:
        try:
            src = os.path.join(src_path, file)
            dst = os.path.join(dest_path, file)
            shutil.move(src, dst)
            print(f"✅ 이동 완료: {file}")
        except Exception as e:
            print(f"⚠️ 이동 실패: {file} | {e}")

def main():
    src_folder = '/Users/jimin/Desktop'       # 원본 위치
    dest_folder = '/Users/jimin/Desktop/images'              # 정리 폴더

    collect_png(src_folder, dest_folder)
    print("\n🎉 SUCCESS! 정리 완료.")

if __name__ == "__main__":
    main()