import random
from tkinter import *


win = Tk()
w = Canvas(win,width=500, height=500)
w.pack()
#tkinter를 500*500으로 출력하기 위한 설정

x_set = range(0,16)
y_set = range(0,7)
#8명에서 게임을 하고 사다리의 갯수는 16개로 설정

x_line=40
y_line=20
line_fin =425
line_gep=25
#tkinter에서 선을 출력하기 위한 변수 선언

w.create_text(180,8,text="A       B        C         D        E        F        G        H")
for i in range(1,9):
    w.create_line(x_line*i,y_line,x_line*i,line_fin)
# 사용자 A~H 까지 출력하고 아래 선을 출력함

map = [[0]*8 for y_set in range(0,16)]
start = []
# 맵을 표시할 배열을 초기화한다
i = 0

#경로 생성
while(i < len(x_set)):
        x = random.choice(x_set)
        y = random.choice(y_set)
        x_tmp=x+1
        y_tmp=y+1
        if(map[x][y] == 0 and map[x][y+1] == 0):
                map[x][y] = map[x][y+1] = 1
                start.append([x,y])
                w.create_line(x_line*y_tmp,line_gep*x_tmp,x_line*(y_tmp+1),line_gep*x_tmp)
                i = i + 1

target = random.randint(0,8)
#도착지를 렌덤으로 생성함
index = len(x_set)-1
print("당첨 : ",target)
print(" A  B  C  D  E  F  G  H")
# 콘솔에서 확인하기 위한 정보 출력

w.create_text(x_line*(target+1),line_fin+30,text=" 당첨!")
# 당첨 정보를 tkinter에 출력

#누가 당첨인지 확인하는 알고리즘
while(index>=0):
        if(map[index][target] == 0):
                index = index - 1
        elif(map[index][target] == 1):
                if([index,target] in start):
                        target = target + 1
                        index = index - 1
                else:
                        target = target - 1
                        index = index - 1
        result = target


for i in range(16):
    print(map[i])
# 전체 맵의 배열 출력

winner = {0:'A',1:'B',2:'C',3:'D',4:'C',5:'F',6:'G',7:'H', }
#도착한 부분을 딕셔러리로 정의해 출력함
p_winner = winner.get(result)
print(p_winner)
w.create_text(200,480,text="당첨자는 :",)
w.create_text(240,480,text=p_winner)
win.mainloop()
#비주얼스튜디오에서 tk을 출력하기 위해 메인루프를 선언함