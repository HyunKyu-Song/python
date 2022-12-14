#! C:\Python39\python.exe
# -*- coding: utf-8 -*-

print("content-type: text/html; charset=utf-8\n")
import sys
import codecs

# stdout의 인코딩을 UTF-8로 강제 변환한다
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print(''' 
<html lang="ko">
<head>
   <meta charset="UTF-8">
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
   <title>index</title>
   <style>
      .title{
         text-align: center;
      }
      .link{
         text-decoration: none;
         color: black;
         text-align: right;
         font-weight: bold;
      }
      .txt1{
         color: red;
      }
      .txt2{
         color: coral;
      }
      .txt3{
         color: yellow;
      }
      .txt4{
         color: green;
      }
      .txt5{
         color: blue;
      }
      .txt6{
         color: darkblue;
      }
      .txt7{
         color: purple;
      }
      img{
         height: 200px;
      }
   </style>
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
   <hr>
   <h2 class="title">웹사이트에 온 걸 환영해!!</h2>
   <hr>
   <img style="float:right" src="./tiger.png" alt="">
   <form action="#">
      <fieldset>
         <legend>필수입력</legend>
         <div>
            <label for="userId">ID</label>
            <input type="text" id="userId" placeholder="아이디 입력" required>
         </div>
         <div>
            <label for="userPw">PW</label>
            <input type="password" id="userPw" placeholder="비밀번호 입력" required>
         </div>
         <button>로그인</button>
      </fieldset>
   </form>
   <br>
   <div>
      <p class="txt1">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt2">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt3">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt4">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt5">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt6">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
      <p class="txt7">
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium facere mollitia corrupti! Quasi, quas quisquam! Modi minima dolor odit itaque at ipsa! Laboriosam odit magnam, ullam quidem sed quaerat dolorem!
      </p>
   </div>

   <script 
   src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js"
   integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa"
   crossorigin="anonymous">
</script>
</body>
</html>
''')
