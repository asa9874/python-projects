import speech_recognition as sr
import konlpy
from konlpy.tag import Okt
okt = Okt()
#import sys #-- 텍스트 저장시 사용

kor_dic={}

r = sr.Recognizer()
while True:
    print("인식중")
    with sr.Microphone() as source:speech = r.listen(source)
    try:
        audio = r.recognize_google(speech, language="ko-KR")
        print(audio)
    except sr.UnknownValueError:print("인식실패")
    except sr.RequestError as e:print("요청실패"+str(e))
    if(audio=="시스템 종료"):break
    print("okt 형태소 추출:", okt.morphs(audio)) 
    




