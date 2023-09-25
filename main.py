from flask import Flask, render_template,request
import pymysql as sql
app=Flask(__name__)
def connect():
    
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/signup/")
def signup():
    return render_template("signup.html")
@app.route("/aftersignup/",methods=['POST','GET'])
def aftersignup():
    if request.method=='GET':
        return render_template("signup.html")
    else:
        name=request.form.get('name')
        email=request.form.get('email')
        passwd=request.form.get('passwd')


if __name__=="__main__":
    app.run(port=80,debug=True)