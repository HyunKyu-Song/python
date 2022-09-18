#! C:\Python39\python.exe
# -*- coding: utf-8 -*-

print("content-type: text/html; charset=utf-8\n")

import sys
import codecs
from tkinter import*
import random
# import matplotlib.image as img
# import matplotlib.pyplot as pp

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print('''
      <head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
   <title>hello.py</title>
</head>
      <body>
   <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
      <a class="navbar-brand" href="index.py">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
         <ul class="navbar-nav">
            <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="index.py">Home</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="hello.py">Other page</a>
            </li>
         </ul>
      </div>
      </div>
   </nav>
   </body>
   <script 
   src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
   integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
   crossorigin="anonymous">
</script>
      ''')
print('<br>');
list = ['새롬', '하영', '규리', '지원', '지선', '서연', '나경', '채영', '지헌']
m = random.randint(0, 8)
# print(list[m])


for i in list:
   print(i + '<br>');

# fileName = "tiger.png"
# ndarray = img.imread(fileName)
# pp.imshow(ndarray)
# pp.show()

# def member():
#    mem = ent.get()
#    print(mem)
   # lab4.config(text = ent.get())


# win = Tk()

# win.title('< 프로미스나인 >')
# win.geometry('1000x500')
# win.option_add('Font*', '궁서 40')

# lab_d = Label(win)
# # img = PhotoImage(file= "C:\\Users\\owner\\Desktop\\단체13.jpeg", master= win)
# # img = PhotoImage(file = "C:\\Users\\owner\\Documents\\대학교 수업 2021-2\\데이터 과학 이해\\팀 과제\\GUI\\promis9.PNG", master = win)
# #img = img.subsample(2)
# # lab_d.config(image = img)
# lab_d.pack()

# lab1 = Label(win)
# lab1.config(text = 'Fromis9')
# lab1.pack()

# ent = Entry(win)
# bt = Button(win)
# bt.config(text = '프롬이들')
# bt.config(command = member)
# bt.pack()
# ent.pack()

# lab4 = Label(win)
# lab4.pack()

# lab2 = Label(win)
# lab2.config(text = 'RAMDOM!!')
# lab2.pack()

# lab3 = Label(win)
# lab3.pack()

# bt2 = Button(win)
# bt2.config(text = '랜덤으로 멤버 이름 뽑기')
# bt2.config(command = ram)
# bt2.pack()

# win.mainloop()