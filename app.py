import sqlite3
from flask import Flask

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('estimating.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS estimates (
                      id INTEGER PRIMARY KEY,
                      item TEXT,
                      quantity INTEGER,
                      price REAL)''')
    conn.commit()
    conn.close()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(host='0.0.0.0', port=80)
