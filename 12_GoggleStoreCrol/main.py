# 필요한 라이브러리 설치 (최초 1회 실행 필요)
# !pip install google-play-scraper pandas openpyxl

from google_play_scraper import reviews_all
import pandas as pd
import re

# 크롤링할 앱 패키지명 리스트
app_packages = ['com.gsr.gs25']

# 요구사항 관련 키워드 정의
keywords = [
    "요구사항", "요청", "필요", "개선", "추가", "제안", "변경", 
    "새로운 기능", "기능 추가", "기능 개선"
]

# 정규표현식 패턴 생성 (대소문자 구분 없이)
regex_keywords = [re.compile(re.escape(kw), re.IGNORECASE) for kw in keywords]

# 필터링 함수
def contains_keyword(text):
    if pd.isna(text):
        return False
    for regex in regex_keywords:
        if regex.search(text):
            return True
    return False

# 각 앱별로 리뷰 크롤링 및 저장
for app_package in app_packages:
    print(f" {app_package} 리뷰 크롤링 중...")
    
    reviews = reviews_all(
        app_package,
        sleep_milliseconds=0,
        lang='ko',
        country='kr'
    )
    df = pd.DataFrame(reviews)
    filtered_df = df[df['content'].apply(contains_keyword)]
    excel_filename = f"filtered_reviews_{app_package}.xlsx"
    filtered_df.to_excel(excel_filename, index=False)
    print(f"{app_package} 필터링된 리뷰 {len(filtered_df)}개 저장 완료: {excel_filename}")

print("모든 앱 리뷰 크롤링 및 필터링 완료!")
