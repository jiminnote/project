import os.path
import shutil # 파일 이동용
from datetime import datetime

# 날짜 기반 폴더 생성 함수
def create_date_folder(base_path):
    today = datetime.today().strftime("%Y-%m-%d") # 오늘 날짜를 %Y-%m-%d 형식의 문자열로 저장
    folder_path = os.path.join(base_path, today)  # base 폴더와 날짜를 붙여서 전체 경로 생성(./organized_files/2025-07-10)
    os.makedirs(folder_path, exist_ok=True) # 해당 경로가 없으면 새로만듬(있으면 아무 일도 안일어남)
    return folder_path

# 소스 폴더안에 있는 파일들만 가져오는 함수
def get_file_list(src_path):
    return [ f for f in os.listdir(src_path) if os.path.isfile(os.path.join(src_path, f))] # 전체 목록 중 파일만 필터링하여 리스트로 반환

# 확장자 기준으로 서브 폴더 정리 함수
def move_files_extension(src_path, dest_path):
    files = get_file_list(src_path) # 정리할 대상 파일 가져옴
    for file in files:
        try:
            ext = file.split(".")[-1] # 확장자 부분 가져옴(예: img.png → png)
            ext_folder = os.path.join(dest_path, file) # (예: organized_files/2025-07-10/png)
            os.makedirs(ext_folder, exist_ok=True) # 확장자 폴더 없으면 만듬
            shutil.move(os.path.join(src_path, file), os.path.join(ext_folder, file)) # 소스path 에서  지정된 확장자 폴더로 이동
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

