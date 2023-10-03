from flask import Flask
# redirect(欲導向的網址)
from flask import redirect  
from flask import render_template 

app = Flask (__name__)

# @app.route('/')
# def welcome():
#     return 'welcome !'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information1')
def information1():
    return render_template("information1.html")

@app.route('/information2')
def information2():
    return render_template("information2.html")

# 2-1
@app.route('/information21')
def information21():
    return render_template("information21.html")

@app.route('/information22')
def information22():
    return render_template("information22.html")


@app.route('/information3')
def information3():
    return render_template("information3.html")

@app.route('/myself')
def myself():
    return render_template("myself.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/others')
def others():
    return render_template("others.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")


@app.route('/report1')
def report1():
    return render_template("report1.html")   

@app.route('/report2')
def report2():
    return render_template("report2.html")  

@app.route('/report3')
def report3():
    return render_template("report3.html")  





if __name__=='__main__':
    app.run()
