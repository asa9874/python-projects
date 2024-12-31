#webp 파일을 jpg 파일로 변환하는 코드
from PIL import Image
import os

def convert_webp_to_jpg(directory):
    # 디렉토리 내 모든 파일 탐색
    for filename in os.listdir(directory):
        # 파일이 .webp 형식인 경우
        if filename.endswith(".webp"):
            webp_path = os.path.join(directory, filename)
            jpg_path = os.path.join(directory, filename.replace(".webp", ".jpg"))
            
            # .webp 파일 열기
            with Image.open(webp_path) as img:
                # RGB 모드로 변환 후 저장
                img.convert("RGB").save(jpg_path, "JPEG")
            print(f"{filename} -> {filename.replace('.webp', '.jpg')} 변환 완료")

#경로적으셈
convert_webp_to_jpg("경로")
