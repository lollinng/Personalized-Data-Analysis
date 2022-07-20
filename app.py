from flask import Flask, render_template, request, redirect, url_for
from df_helper import helper
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/BE', methods=['GET', 'POST'])
def BE():
    if request.method == 'POST':
        roll_no = request.form['roll']
        print(roll_no)
        obj = helper()
        obj.BEfunction(roll_no)
        return render_template("dynamic.html", std="BE")
    return render_template("BE.html")


@app.route('/SE', methods=['GET', 'POST'])
def SE():
    if request.method == 'POST':
        roll_no = request.form['roll']
        print(roll_no)
        obj = helper()
        obj.SEfunction(roll_no)
        return render_template("dynamic.html", std="SE")
    return render_template("SE.html")


@app.route('/TE', methods=['GET', 'POST'])
def TE():
    if request.method == 'POST':
        roll_no = request.form['roll']
        print(roll_no)
        obj = helper()
        obj.TEfunction(roll_no)
        return render_template("dynamic.html", std="TE")
    return render_template("TE.html")


@app.route('/defaultSE', methods=['GET', 'POST'])
def defaultSE():
    df = pd.read_excel('attendance.xlsx', sheet_name='SE')
    obj = helper()
    ans = obj.defaulters(df)
    length = len(ans[0])
    return render_template("default.html", ans=ans, length=length)


@app.route('/defaultBE', methods=['GET', 'POST'])
def defaultBE():
    df = pd.read_excel('attendance.xlsx', sheet_name='BE')
    obj = helper()
    ans = obj.defaulters(df)
    length = len(ans[0])
    return render_template("default.html", ans=ans, length=length)


@app.route('/defaultTE', methods=['GET', 'POST'])
def defaultTE():
    df = pd.read_excel('attendance.xlsx', sheet_name='TE')
    obj = helper()
    ans = obj.defaulters(df)
    length = len(ans[0])
    return render_template("default.html", ans=ans, length=length)


if __name__ == "__main__":
    app.secret_key = "Secret Key"
    app.run(debug=True)
