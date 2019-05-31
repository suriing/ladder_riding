from tkinter import *
import random

win = Tk()
w = Canvas(win,width=500, height=500)
w.pack()

x_line=40
y_line=20
line_fin =450
line_gep=25
w.create_text(180,8,text="A       B        C         D        E        F        G        H")
for i in range(1,9):
    w.create_line(x_line*i,y_line,x_line*i,line_fin)


x_set = range(0,16)
y_set = range(0,7)

map = [[0]*8 for i in range(0,16)]

start = []
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

win.mainloop()