# !pip install google-play-scraper pandas openpyxl

from google_play_scraper import reviews_all
import pandas as pd

# 크롤링할 앱의 패키지명을 입력
app_package = 'com.gsr.gs25' 
reviews = reviews_all(
    app_package,
    sleep_milliseconds=0,   
    lang='ko',              
    country='kr'          
)

df = pd.DataFrame(reviews)
excel_filename = "app_reviews.xlsx"
df.to_excel(excel_filename, index=False)

print(f"총 {len(df)}개의 리뷰가 '{excel_filename}' 파일로 저장되었습니다.")
