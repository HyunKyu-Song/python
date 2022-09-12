from flask import Flask, render_template

app = Flask(__name__)

@app.route('/apple')
def a():
   return '''
         apple은 사과맞쥬?<br>
         <a style="color: coral;" href="/">home</a>
      '''

# @app.route('/promis')
# def a():
#    return render_template("test1.py")

@app.route('/')
def index():
   return render_template("index.html")
   # return """
   #          <h1>Flask를 사용한 웹서버 가즈아~</h1>
   #          <p>apple은 사과</p>
   #          <a style="color: coral;" href="/apple">사과 페이지로 가자!</a>
   #       """

if __name__ == '__main__':
   app.run(debug=True)
