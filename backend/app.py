from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database (or create it if it doesn't exist)
def connect_db():
    conn = sqlite3.connect('data.db')
    return conn

# Initialize the database
def init_db():
    conn = connect_db()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value1 TEXT NOT NULL,
                value2 TEXT NOT NULL
            )
        ''')
    conn.close()

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    value1 = data.get('value1')
    value2 = data.get('value2')

    if not value1 or not value2:
        return jsonify({'error': 'Both value1 and value2 are required'}), 400

    conn = connect_db()
    with conn:
        conn.execute('INSERT INTO data (value1, value2) VALUES (?, ?)', (value1, value2))
    conn.close()

    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

