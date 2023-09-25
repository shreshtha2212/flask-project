from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("one.html")
@app.route("/home/<name>/<int:age>")
def home(name,age):
    return render_template("one.html",n=name,a=age)
@app.route("/marks/<int:maths>/<int:sci>/<int:eng>/")
def marks(maths,sci,eng):
    data={
        "Maths":maths,
        "Science":sci,
        "English":eng,
        "Percentage": round((maths+sci+eng)/3,2)
    }
    return render_template("one.html",data=data)
if __name__=="__main__":
    app.run(port=80,debug=True)