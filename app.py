from flask import Flask,request,render_template
from util import database

app = Flask(__name__)

def counter(n=10):
    for i in range(1, n+1):
        yield i

@app.route("/", methods = ["GET", "POST"])
def gfg():
    
    if request.method == "POST":
        username = request.form.get("fname")
        password = request.form.get("lname") 
        
        for i in database.all_users():
            if username == i[0] and password == i[1]:
                return render_template("hello.html",username=username,password=password)
        
        return "error"
    return render_template("login.html")
    

@app.route("/count")
def count():
    """
    1
    2
    3
    4
    5
    ...
    """
    lst = [1,2,3]
    lst[10] += 1
    return render_template("count.html", content=counter())
    
@app.route("/child")
def child():
    return render_template("child.html")

if __name__ == "__main__":
    app.debug = True
    app.run()