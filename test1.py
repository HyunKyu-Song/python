from tkinter import*
import random

def ram():
   list = ['새롬', '하영', '규리', '지원', '지선', '서연', '나경', '채영', '지헌']
   m = random.randint(0, 8)
   #print(list[m])
   lab3.config(text = list[m])


def member():
   mem = ent.get()
   #print(mem)
   lab4.config(text = ent.get())


win = Tk()

win.title('< 프로미스나인 >')
win.geometry('1000x500')
win.option_add('Font*', '궁서 40')

lab_d = Label(win)
# img = PhotoImage(file= "C:\\Users\\owner\\Desktop\\단체13.jpeg", master= win)
# img = PhotoImage(file = "C:\\Users\\owner\\Documents\\대학교 수업 2021-2\\데이터 과학 이해\\팀 과제\\GUI\\promis9.PNG", master = win)
#img = img.subsample(2)
# lab_d.config(image = img)
lab_d.pack()

lab1 = Label(win)
lab1.config(text = 'Fromis9')
lab1.pack()

ent = Entry(win)
bt = Button(win)
bt.config(text = '프롬이들')
bt.config(command = member)
bt.pack()
ent.pack()

lab4 = Label(win)
lab4.pack()

lab2 = Label(win)
lab2.config(text = 'RAMDOM!!')
lab2.pack()

lab3 = Label(win)
lab3.pack()

bt2 = Button(win)
bt2.config(text = '랜덤으로 멤버 이름 뽑기')
bt2.config(command = ram)
bt2.pack()

win.mainloop()