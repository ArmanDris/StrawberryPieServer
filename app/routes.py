from flask import render_template, request, jsonify
from . import app
import sqlite3

@app.route('/')
def home_page():
    return ('Hello world!')
    # return render_template('index.html')

# @app.route('/ping')
# def handle_ping():
#     return jsonify({'message':'ok'}), 200

# @app.route('/mailbox', methods=['POST'])
# def handle_mail():
#     conn = sqlite3.connect('leaderboard.db')
#     c = conn.cursor()
#     try:
#         name = request.json['name']
#         time = int(request.json['time'])
#         difficulty = request.json['difficulty']

#         if not name or not time or not difficulty:
#             return jsonify({'error': 'Missing JSON data'}), 400
        
#         print(name + " got " + str(time) + " on " + difficulty)

#         c.execute("INSERT INTO leaderboard (name, time, difficulty) VALUES (?, ?, ?)", (name, time, difficulty))
#         conn.commit()
#         conn.close()
#         return jsonify({'message': (name + " got " + str(time) + " on " + difficulty)}), 200
    
#     except Exception as e:
#         print(f'An error occurred: {e}')
#         conn.close()
#         return jsonify({'error': 'Internal Server Error'}), 500
    
# @app.route('/leaderboard', methods=['POST'])
# def send_leaderboard():
#     conn = sqlite3.connect('leaderboard.db')
#     c = conn.cursor()
#     try:
#         c.execute("SELECT name, time, difficulty FROM leaderboard ORDER BY time ASC LIMIT 15")
#         rows = c.fetchall()
#         conn.close()
#         return jsonify({'leaderboard': rows}), 200
    
#     except Exception as e:
#         print('An error occured', str(e))
#         conn.close()
#         return jsonify('error', 'internal server error'), 500