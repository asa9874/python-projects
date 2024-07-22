import requests
import json
import datetime
from datetime import datetime  as dt
import pprint
import time
key_lol='라이엇 키를 입력해주세요'
headers_lol= {"X-Riot-Token":key_lol} 
nickname_lol="검색할 닉네임을 검색해주세요"
match_list=[]
core_nick_list=["매칭내부에 들어가야하는 인원적어주세요"]


#매치 클래스
class match():
    
    #생성
    def __init__(self,game_duration,game_creation,game_Mode,player):
        self.duration=str(datetime.timedelta(seconds=game_duration))     #매치 플레이시간
        self.creation=str((dt.fromtimestamp(game_creation/1000)).strftime('%Y/%m/%d %H시 %M분 %S초'))         #게임시작시간
        self.mode=game_Mode                                              #맵
        self.players=player                                         #플레이어 리스트
        self.core_players=[]

    #내가알고싶은애들 넣기
    def set_core_player(self):
        list1=[]
        for i in self.players:
            if (i.nickname in core_nick_list): self.core_players.append(i)



    #출력
    def print_data(self):
        print("닉네임:"+str(self.players[0].nickname))
        print("게임길이:"+str(self.duration))
        print("챔피언:"+str(self.players[0].champion))
        print("킬:"+str(self.players[0].kills))
        print("데스:"+str(self.players[0].deaths))
        print("어시:"+str(self.players[0].assists))
        print("죽어있던시간:"+str(self.players[0].dead_time))
        print("딜량:"+str(self.players[0].total_damage))
        print("받은딜량:"+str(self.players[0].total_taken_damgage))

    #알고싶은 애들 출력
    def print_core_data(self):

        print("게임길이:"+str(self.duration))
        print("게임형식:"+self.mode)
        print("게임시작시간:"+self.creation)


        for player in self.core_players:
            print("닉네임:"+str(player.nickname))
            print("승리?:"+str(player.win)) 
            print("챔피언:"+str(player.champion))
            print("킬:"+str(player.kills))
            print("데스:"+str(player.deaths))
            print("어시:"+str(player.assists))
            print("죽어있던시간:"+str(player.dead_time))
            print("딜량:"+str(player.total_damage))
            print("받은딜량:"+str(player.total_taken_damgage))


#닉,딜같은 게임의 플레이어정보 
class player():
    def __init__(self,nickname,champion,kills,deaths,assists,win,dead_time,total_damage,total_taken_damage):
        self.nickname=nickname
        self.champion=champion
        self.kills=kills
        self.deaths=deaths
        self.assists=assists
        if win=="True": self.win="승리"
        else: self.win="패배"
        self.dead_time=str(datetime.timedelta(seconds=dead_time))
        self.total_damage=total_damage
        self.total_taken_damgage=total_taken_damage 


#api 데이터 크롤링
class crol_lol():
    #puuid 얻기
    def get_puuid(nickname):
        url_lol='https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nickname
        r= requests.get(url_lol,headers=headers_lol)
        return r.json()['puuid'] #고유 puuid

    #게임기록들얻기
    def get_matchs(nickname):
        lol_puuid=crol_lol.get_puuid(nickname)
        
        #r=requests.get('https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/'+lol_puuid+'/ids?start=0&count=20',headers=headers_lol)
        now = time.time()
        diff=43200+1000000
        start_time=now-diff #12시간전
    
        r=requests.get('https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/'+lol_puuid+'/ids?startTime='+str(int(start_time))+'&start=0&count=20',headers=headers_lol)
        return r.json() #게임 기록들

    #게임 세부사항얻기
    def get_gamedata(nickname):
        lol_matchs=crol_lol.get_matchs(nickname_lol)        #12시간 내부의 게임 매치들 
        for lol_match in lol_matchs:
            player_list=[]
    

            r=requests.get('https://asia.api.riotgames.com/lol/match/v5/matches/'+lol_match,headers=headers_lol)
            game_duration=r.json()['info']['gameDuration']                                          #게임길이(초시간)
            game_creation=r.json()['info']['gameCreation']                                          #게임시작시간(타임스탬프)
            game_Mode=r.json()['info']['gameMode']                                                  #게임맵



            for i in range(10):
                game_nickname=r.json()['info']['participants'][i]['summonerName']                       #플레이어 이름
                game_champion=r.json()['info']['participants'][i]['championName']                       #챔프이름
                game_kills=r.json()['info']['participants'][i]['kills']                                 #킬
                game_deaths=r.json()['info']['participants'][i]['deaths']                               #데스
                game_assists=r.json()['info']['participants'][i]['assists']                             #어시스트
                game_win=r.json()['info']['participants'][i]['win']                                     #승패 bool 형식
                game_dead_time=r.json()['info']['participants'][i]['totalTimeSpentDead']                #뒤져있던 시간(초시간)
                game_total_damage=r.json()['info']['participants'][i]['totalDamageDealtToChampions']    #딜량
                game_total_taken_damage=r.json()['info']['participants'][i]['totalDamageTaken']         #받은 피해량
                player_list.append(player(game_nickname,game_champion,game_kills,game_deaths,game_assists,game_win,game_dead_time,game_total_damage,game_total_taken_damage))#플레이어 10명데이터
            match_list.append(match(game_duration,game_creation,game_Mode,player_list))
            print("게임데이터 불러오기 완료")
        print("게임데이터 불러오기 모두 완료")


crol_lol.get_gamedata(nickname_lol)
match_list[0].set_core_player()
match_list[0].print_core_data()



