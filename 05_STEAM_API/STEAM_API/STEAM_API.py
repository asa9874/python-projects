import requests
from steam import Steam
import pprint
import time

#게임이름, 게임가격 리턴해주는 함수
def nameprice_check(i):
    name=i["name"]

    try:#유료
        
        price=steam.apps.search_games(name)["apps"][0]["price"]
        if (price[0] != '$'):
            price=0
        else:
            price=float(price[1:])*1000
    except:#무료 
        price=0

    return name,price

#게임 가격 합산
def pricesum(price_list):
    sumprice=0
    for i in price_list:
        sumprice=sumprice+i

    return sumprice



#스팀 api 설정
Key="발급받은 API 키 입력해주세용"
steam = Steam(Key)
my_ID="얻을 스팀 ID 를 입력해주세용"
#아이디 입력받아 식별코드 얻기
ID=steam.users.search_user("my_ID")["player"]["steamid"]

#게임목록 추출(리스트)
game=steam.users.get_owned_games(ID)["games"]

#게임 가격모음
game_price_list=[]
gamenum=0

#게임 가격 하나하나하기
for i in game:
    gamenum=gamenum + 1
    game_name,game_price=nameprice_check(i)
    pprint.pprint("게임: "+game_name + "가격:" + str(game_price) +"원")

    
    game_price_list.append(game_price)

#가격합산
gamesum=pricesum(game_price_list)

print(str(gamenum)+"\t"+str(gamesum))