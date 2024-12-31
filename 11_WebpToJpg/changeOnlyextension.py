#오직 확장자 이름만 변경하는 코드입니다.
import os

def change_extension(directory):
    # 디렉토리 내 모든 파일 탐색
    for filename in os.listdir(directory):
        # 파일이 .webp 형식인 경우
        if filename.endswith(".webp"):
            webp_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace(".webp", ".jpg"))
            
            # 파일 이름 변경
            os.rename(webp_path, jpg_path)
            print(f"Renamed {filename} to {filename.replace('.webp', '.jpg')}")

#경로적으셈
change_extension(r"C:\Users\asa\Desktop\dataset")
