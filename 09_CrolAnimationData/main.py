import selenium
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import time
import json

#크롬 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 자동화기계 방지 뚫기+프로필위조 (가끔 selenium을 자동화기계로 오인해서 차단하는 사이트들이 있다는데.. (사실 오인이 아니다) 이를 방지하기 위해 프로필을 위조한다.)
chrome_options.add_argument("disable-gpu")   # GPU가속 끄기
chrome_options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 위조
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) #자동화된 소프트웨어 제어 문구 삭제
chrome_options.add_argument(r'user-data-dir=C:\User Data')
# 브라우저 생성
browser = webdriver.Chrome(options=chrome_options)



#분기 링크리스트제작
def GetQuarterLink():
    QuarterLinkList=[]
    baseLink="https://anime.onnada.com/"
    time.sleep(1)
    for year in range(2000,2025):
        for quarter in range(1,5):
            QuarterLinkList.append(baseLink+str(year)+"."+str(quarter)+".php")
    return QuarterLinkList


#애니메이션 링크 얻기
def GetAnimationLink(QuarterLinkList):
    time.sleep(0.5)
    AnimationLinkList=[]
    AnimeList=browser.find_elements(By.CLASS_NAME, "title")
    for element in AnimeList:
        try:
            a_tag = element.find_element(By.TAG_NAME, "a")
            href = a_tag.get_attribute("href")
            #print(href)
            AnimationLinkList.append(href)
        except:
            continue
    return AnimationLinkList


#애니메이션 데이터얻기
def GetAnimationData():
    time.sleep(0.2)
    try:
        AnimationName=browser.find_elements(By.TAG_NAME,"h1")[0].text
        AnimationImage=browser.find_elements(By.CLASS_NAME,"image")[0].find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "a").get_attribute("href")
        AnimationInfoList=browser.find_elements(By.CLASS_NAME,"list")[0].find_elements(By.TAG_NAME, "p")
        
        for Animationinfo in AnimationInfoList:
            Year=Animationinfo.find_elements(By.CLASS_NAME, "block")[1].text
            if(Year[:2]=='20'):
                AnimationYear=Year.split(" ")[0].replace('.','-')
                break

        Animationinfo = {
            "AnimationName": AnimationName,
            "AnimationImg": AnimationImage,
            "AnimationYear": AnimationYear
        }
        AnimationinfoList.append(Animationinfo)
        print(Animationinfo,end="")
        print(",")


    except:
        #print("GetAnimationData 예외발생")
        return
    

#애니정보리스트
AnimationinfoList=[]
#분리 리스트
QuarterLinkList=GetQuarterLink()

#이후 분기리스트 반복
for QuarterLink in QuarterLinkList:
    browser.get(QuarterLink)

    #애니리스트얻기
    AnimationLinkList=GetAnimationLink(QuarterLink)

    #각 애니데이터 얻기
    for AnimationLink in AnimationLinkList:
        browser.get(AnimationLink)
        GetAnimationData()


with open("animations.json", "w", encoding="utf-8") as json_file:
    json.dump(AnimationinfoList, json_file, ensure_ascii=False, indent=4)


