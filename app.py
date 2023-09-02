import os
import sqlite3
from flask import Flask, flash, render_template, redirect, session, url_for, g
from flask.globals import request
from werkzeug.utils import secure_filename
from Asummary import load_model_and_tokenizer, summarize_text as summarize_pegasus
from Esummary import load_model, summarize_text as summarize_summarizer
from mcq import MCQs
import re
from qa import QAEvaluator,QuestionGenerator

#constants
questionLength = 0
text=""

app = Flask(__name__)

currentLocation = os.path.dirname(os.path.abspath(__file__))
app.secret_key = 'MYINTELLIQ'
pegasus_model, pegasus_tokenizer = load_model_and_tokenizer('model.pkl')
summarizer_model = load_model('summarizer_model.pkl')

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return redirect('/')


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@ app.route('/')
def index():
    """ The landing page for the app from scratch """
    return render_template('index.html')


@ app.route('/signin')
def signin():
    return render_template('signin.html')

@ app.route('/signin', methods=['POST'])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.Connection(currentLocation+"\\Login.db")
    cursor = sqlconnection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users(Username text, Password text);")
    sqlconnection.commit()
    query1 = "SELECT Username, Password from Users WHERE Username = '{un}' AND Password = '{pw}'".format(un = UN, pw = PW)

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) == 1:
        if request.method == 'POST':
            session.pop('user', None)
            
            if request.form['Password'] == PW:
                session['user'] = request.form['Username']
                return redirect('/upload')


    else:
        flash("❌ Invalid credentials! Try again or sign up!")
    return render_template('signin.html')


@ app.route('/signup', methods=['GET','POST'])
def registerpage():
    if request.method == "POST":
        dUN = request.form['DUsername']
        dPW = request.form['DPassword']
        cPW = request.form['confPw']
        sqlconnection = sqlite3.Connection(currentLocation+"\\Login.db")
        cursor = sqlconnection.cursor()
        try:
            if cPW == dPW:
                checkUser = "SELECT Username, Password from Users WHERE Username = '{dun}' AND Password = '{dpw}'".format(dun = dUN, dpw = dPW)
                rows = cursor.execute(checkUser)
                rows = rows.fetchall()
                if len(rows) == 1:
                    flash("❗ User already exists, try logging in!")
                else:
                    query1 = "INSERT INTO Users VALUES('{u}','{p}')".format(u = dUN, p = dPW)
                    cursor.execute(query1)
                    sqlconnection.commit()
                    flash("🎉 Awesome! Account created, now log in to your account!")
                    return redirect('/signin')
            else:
                flash("🤨 Password and Confirm password don't match, try again!")
                return render_template('signup.html')
        except:
            flash("⛔ Unknown error occured, try again later!")
            return render_template('signup.html')
    return render_template('signup.html')

@ app.route('/upload')
def upload():
    if g.user:
        return render_template('upload.html')
    return render_template('unauthorized.html')

@ app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global text
    text = request.form['input-text']
    return render_template(
        'quiz.html')



@app.route('/ab_summary', methods=['POST'])
def ab_summary():
    global text
    summary = summarize_pegasus(text, pegasus_model, pegasus_tokenizer)
    summary = summary.replace("<pad>", "").replace("</s>", "")
    return render_template('ab_summary.html', text=text, summary=summary)

@app.route('/ex_summary', methods=['POST'])
def ex_summary():
    global text
    summary = summarize_summarizer(text, summarizer_model)
    return render_template('ex_summary.html', text=text, summary=summary)

@app.route('/qaa', methods=['POST'])
def qaa():
    global text
    x = request.form['myNumber']
    y=int(x)
    generator = QuestionGenerator()
    question = generator.generate(text,num_questions=y)
    return render_template('qaa.html', text=text, question=question)


@app.route('/mq', methods=['POST'])
def mq():
    global text
    mcq=MCQs(text)
    return render_template('mq.html', text=text, mcq=mcq)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')