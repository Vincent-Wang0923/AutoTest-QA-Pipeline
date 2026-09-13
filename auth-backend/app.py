import sqlite3
from flask import Flask,request,jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)
CORS(app)

def get_db_connection():
    conn=sqlite3.connect('demo.db')
    conn.row_factory=sqlite3.Row
    return conn

#Initialize database table
with app.app_context():
    conn=get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/api/register',methods=['POST'])
def register():
    data=request.get_json()
    username=data.get('username','').strip()
    password=data.get('password','').strip()

    if not username or not password:
        return jsonify({'status':'error','message':'Username and password required'}),400

    #Intentional bug
    hashed_pw=generate_password_hash(password)
    conn=get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',(username,hashed_pw))
        conn.commit()
        return jsonify({'status':'success','message':'Registration successful'}),201
    except sqlite3.IntegrityError:
        return jsonify({'status':'error','message':'Username already exists'}),409
    finally:
        conn.close()

@app.route('/api/login',methods=['POST'])
def login():
    data=request.get_json()
    username=data.get('username','').strip()
    password=data.get('password','').strip()

    conn=get_db_connection()
    user=conn.execute('SELECT * FROM users WHERE username = ?',(username,)).fetchone()
    conn.close()

    if user and check_password_hash(user['password_hash'],password):
        return jsonify({'status':'success','message':'Login successful','user_id':user['id']}),200
    else:
        return jsonify({'status':'error','message':'Invalid credentials'}),401

if __name__=='__main__':
    app.run(debug=True,port=5000)