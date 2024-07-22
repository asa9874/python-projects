import csv
import random

#단어 클래스
class VOCA:
    voca_num=0
    def __init__(self,en,kor):
        self.en=en
        self.kor=kor

        
    
#엑셀파일 읽기
def readcsv():
    f=open('english.csv','rt',encoding="CP949")
    rdr = csv.reader(f)

    for line in rdr:
        e=VOCA(line[0],line[1])
        Voca_list.append(e)

#단어장 출력
def print_voca(vo):
    cnt=0;
    for i in vo:
        if(cnt==240):break
        print("\""+i.kor+"\":"+"\""+i.en+"\",")
        cnt+=1




Voca_list=[]  
readcsv()

print_voca(Voca_list)

