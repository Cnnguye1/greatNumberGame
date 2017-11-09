from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'be_nice'


@app.route('/')
def greatNumberGame():
    if 'numb' not in session:
        session['numb']= random.randrange(0, 101)
    print session['numb']
    return render_template('index.html')

@app.route('/guess', methods =['POST'])
def guess():
    session['guess'] = int(request.form['number'])
    return redirect('/')
@app.route('/again')
def again():
    session.pop('numb')
    session.pop('guess')
    return redirect('/')


app.run(debug = True)