import json
import sys
import wtforms
import redis
import random
import string
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from collections import defaultdict
import math
from jinja2 import Environment, meta
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired
import datetime
import string


APPLICATION_NAME='IAUM HighPerformance Computing LAb IHPCL'
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
app.config['WTF_CSRF_SECRET_KEY'] = 'Insert_random_string_here'
app.secret_key = 'bla bla bla?'#secret session



##key
now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year
# node1=15
# node2=16
# node3=17
# random=random.randrange(0, 100, 2)
random = random.random()
s = []
s.append(year)
s.append(month)
s.append(day)
s.append(random)
key = "".join("{0}".format(n) for n in s)




###Redis define data store
REDIS_DB = 0
REDIS_PORT = 6379
REDIS_HOST = 'localhost'
r = redis.Redis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)
###





#index
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


#login checking
@app.route('/login')
def login():
	    
	    return render_template('login.html')


##for return
@app.route('/success')
def success():
	return render_template('success.html')


#register form
@app.route('/register', methods=('GET', 'POST'))
def submit():
    form = Myform()
    if form.validate_on_submit():
        name = request.form['name']
        fname = request.form['fname']
        stid = request.form['stid']
        mainkey = key
        title = request.form['title']
        prof = request.form['prof']
        grade = request.form['grade']
        detail = request.form['detail']
        r.sadd("test:%s:up" %key,"name:%s" %name,"fname:%s" %fname,"stid:%s" %stid,"mainkey:%s" %mainkey,"title:%s" %title,"prof:%s" %prof,"grade:%s" %grade,"detail:%s" %detail)
        # pri #fuckbber
        return redirect('/success')
    return render_template('register.html', form=form)


#Form
class  Myform(Form):
    name = TextField('First name ', validators=[DataRequired()])
    fname = TextField('Last name',validators=[DataRequired()])
    stid = TextField('Student Id',validators=[DataRequired()]) #student id
    title = TextField('Title of request',validators=[DataRequired()])
    prof = TextField('Name of the Profossor',validators=[DataRequired()])
    grade = TextField('grade',validators=[DataRequired()])
    detail= TextField('Detail of Project',validators=[DataRequired()])








##webserver
if __name__ == '__main__':
	app.debug = True
	app.run(host='localhost',port=5000)
