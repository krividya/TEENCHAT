from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from datetime import datetime, timedelta, date
import datetime
import requests, json
import os

app = Flask('app')
app.debug = True
app.secret_key = os.environ.get("APP_SECRET")

try:
    app.config["MONGO_URI"] = os.environ.get("DBURI")
    mongo = PyMongo(app)
    print("connected!")
except:
    print("Cannot connect")

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    session.pop('username', None)
    print("User logged out")
    return render_template("login.html")
  else:
    email = request.form.get('email')
    password = request.form.get('password')
    db_info = mongo.db.user.find({})
    success = False
    for user in db_info: 
      if (email == user["email"] and password == user["p"]):
        success = True 
        session['username'] = user["username"]
        print(session['username'])
        return redirect(url_for('index', user=user["username"]))
    else:
      message = "Invalid credentials"
      return redirect(url_for('login'))    

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template("register.html")
  else: 
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    email_db = mongo.db.user.find({})
    success = True
    
    for user in email_db:
      if email == user["email"]:
        message = "Email already exists. Please try again."
        print(message)
        success = False
        return redirect(url_for('register'))
      elif username == user["username"]:
        message = "Username already exists. Please try again."
        print(message)
        success = False
        return redirect(url_for('register'))
      elif password1 != password2: 
        message = "Passwords do not match. Please try again."
        print(message)
        success = False
        return redirect(url_for('register')) 
    
    if success == True:
      mongo.db.user.insert_one({"name":name, "username":username, "email":email, "p":password1})
      session["username"] = username
      return redirect(url_for('index', user=username))

@app.route('/logout')
def logout():
  session.pop('username', None)
  print("User Logged out")
  return redirect(url_for('index_1'))

@app.route('/home/<user>', methods=['GET', 'POST'])
def index(user):
  if request.method == 'GET':
    return render_template("index.html", user=user)

@app.route("/")
def index_1():
  return render_template("home.html")

@app.route('/chat/<user>', methods=['GET', 'POST'])
def chat(user): 
  if request.method == 'GET':
    user_list = mongo.db.user.find({})
    user_list1 = mongo.db.user.find({})
    return render_template("chat.html", user_list=user_list, user_list1=user_list1, user=user)
  else:
    user_selected = request.form.get('user')
    print(user_selected)
    return redirect(url_for('chat2', user=user, user2=user_selected))

@app.route('/chat/<user>/<user2>', methods=['GET', 'POST'])
def chat2(user, user2):
  if request.method == 'GET':
    messages = mongo.db.message.find({})
    return render_template('chat2.html', user=user, user2=user2, messages=messages)
  else:
    message = request.form.get('message')
    user_from = user
    user_to = user2
    times = datetime.datetime.now()
    mongo.db.message.insert_one({"user_from":user_from, "user_to":user_to, "message":message, "time":times})
    return redirect(url_for('chat2', user=user_from, user2=user_to))

@app.route('/learn/<user>', methods=['GET', 'POST'])
def learn(user):
  if request.method == 'GET':
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    data = mongo.db.state.find({})
    return render_template("learn.html", states=states, data=data, user=user)

@app.route('/creators/<user>', methods=['GET'])
def creators(user):
  if request.method == 'GET':
    return render_template("creators.html", user=user)

@app.route('/getdata', methods=['GET', 'POST'])
def api():
  data = requests.get("https://covidtracking.com/api/states")
  # rest = res.json()
  statelist = json.loads(data.content.decode("utf-8"))
  for record in statelist:
    print(record)
    mongo.db.state.update_one(
      {"state":record["state"]}, 
      {"$set":{"state":record["state"], "date":record["date"], "positive":record["positive"]}}, upsert=True)
  return render_template("learn.html")

app.run(host='0.0.0.0', port=8080)