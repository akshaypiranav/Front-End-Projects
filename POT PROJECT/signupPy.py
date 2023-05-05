from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database configuration
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT NOT NULL,
             password TEXT NOT NULL,
             email TEXT NOT NULL);''')
conn.commit()

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']


    cursor = conn.cursor()
    query = "INSERT INTO users (username, password) VALUES (?, ?)"
    values = (username, password)
    cursor.execute(query, values)
    conn.commit()

    return "Sign up successful!"