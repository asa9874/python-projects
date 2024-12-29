#디씨콘 다운받기

import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import os

# 크롬 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 자동화 기계 방지 및 프로필 위조
chrome_options.add_argument("disable-gpu")   # GPU 가속 끄기
chrome_options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 위조
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 자동화된 소프트웨어 제어 문구 삭제
chrome_options.add_argument(r'user-data-dir=C:\User Data')

# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# 이미지 다운로드 함수
def download_image_with_cookies(src, folder, file_name, driver):
    try:
        # Selenium에서 쿠키 추출
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])

        # 요청 보내기
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Referer": driver.current_url,  # 현재 페이지 URL을 Referrer로 설정
        }
        response = session.get(src, headers=headers, stream=True)

        if response.status_code == 200:
            with open(os.path.join(folder, file_name), 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Successfully downloaded: {file_name}")
        else:
            print(f"Failed to download {src}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading {src}: {e}")

def download_images_from_url(target_url, output_folder):
    create_folder(output_folder)

    try:
        # URL 열기
        browser.get(target_url)
        time.sleep(2)  # 페이지 로딩 대기

        # 이미지 요소 찾기
        images = browser.find_elements(By.TAG_NAME, 'img')

        for i, img in enumerate(images):
            src = img.get_attribute('src')
            if src and 'dccon.php' in src:  # 쿼리 형태 필터링
                print(f"Downloading image {i + 1}: {src}")
                file_name = f"image_{i + 1}.jpg"  # 기본적으로 jpg 확장자 지정
                download_image_with_cookies(src, output_folder, file_name,browser)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.quit()

if __name__ == "__main__":
    url = input("URL입력:")
    output_dir = "downloaded_images"
    download_images_from_url(url, output_dir)
    print("다운완료")
