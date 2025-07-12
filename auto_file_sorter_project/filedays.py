# 파일별 수정일 / 확장자 기준으로 정리

import os
import shutil
import argparse
from datetime import datetime

# 파일의 수정일 얻어오는 함수
def get_file_date(path):
    t = os.path.getmtime(path)
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d') # 파일의 마지막 수정시간을 초단위(fromtimestamp)로 가져옴

# 수정일 기준 + 확장자 폴더로 정리하는 함수
def move_files_date(src_path, dest_path):
    for file in os.listdir(src_path): # 원본 폴더에 있는 모든 항목에 대해 반복
        file_path = os.path.join(src_path, file) # 전체 파일 경로 생성
        if os.path.isfile(file_path): # 
            try:
                mod_date = get_file_date(file_path) # 해당 항목의 수정일 구함
                dest_folder = os.path.join(dest_path, mod_date) # 날짜별 폴더 생성 경로 구성

                ext = file.split(".")[-1] # 파일의 확장자 추출
                ext_folder = os.path.join(dest_folder, ext) # 날짜폴더 안에 확장자별 하위 폴더 경로 구성 (예: ./screenshots/2025-07-10/png)
                os.makedirs(ext_folder, exist_ok=True) # 폴더가 없으면 새로 만들고, 있으면 유지

                shutil.move(file_path, os.path.join(ext_folder, file)) # 해당 파일을 새 폴더로 이동
                print(f"{file}->{mod_date}/{ext}/") # 로그 출력
            except Exception as e:
                print(e)

def main() :
    parser = argparse.ArgumentParser(description="📂 파일을 날짜 + 확장자별로 정리하는 스크립트")
    parser.add_argument('--src',type=str, required=True, help='원본 폴더 경로')
    parser.add_argument('--dest', type=str, required=True, help='정리된 파일이 저당될 폴더 경로')

    args = parser.parse_args()

    if not os.path.exists(args.src):
        print("No Exist!!")
        return

    move_files_date(args.src, args.dest)
    print("SUCCESS!!")
if __name__ == "__main__":
    main()
