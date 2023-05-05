
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
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    

    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=? AND password=?"
    values = (username, password)
    cursor.execute(query, values)
    user = cursor.fetchone()

    if user:
        return f"Welcome, {username}!"
    else:
        return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)