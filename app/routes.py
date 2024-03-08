from flask import render_template, request, jsonify, Blueprint, current_app
import sqlite3
from .db import get_db, close_db

bp = Blueprint('bp', __name__)

@bp.route('/')
def home_page():
    return render_template('index.html')

@bp.route('/ping')
def handle_ping():
    return jsonify({'message':'ok'}), 200

@bp.route('/mailbox', methods=['POST'])
def handle_mail():
    db_name = current_app.config['DATABASE']
    conn = get_db(db_name)
    c = conn.cursor()
    try:
        name = request.json['name']
        time = int(request.json['time'])
        difficulty = request.json['difficulty']

        if not name or not time or not difficulty:
            return jsonify({'error': 'Missing JSON data'}), 400
        
        print(name + " got " + str(time) + " on " + difficulty)

        c.execute(f"INSERT INTO {current_app.config['DATABASE']} (name, time, difficulty) VALUES (?, ?, ?)", (name, time, difficulty))
        conn.commit()
        close_db()
        return jsonify({'message': (name + " got " + str(time) + " on " + difficulty)}), 200
    
    except Exception as e:
        print(f'An error occurred: {e}')
        close_db()
        return jsonify({'error': 'Internal Server Error'}), 500
    
@bp.route('/leaderboard', methods=['POST'])
def send_leaderboard():
    db_name = current_app.config['DATABASE']
    conn = get_db(db_name)
    c = conn.cursor()
    try:
        c.execute(f"SELECT name, time, difficulty FROM {current_app.config['DATABASE']} ORDER BY time ASC LIMIT 15")
        rows = c.fetchall()
        close_db()
        return jsonify({'leaderboard': rows}), 200
    
    except Exception as e:
        print('An error occured', str(e))
        close_db()
        return jsonify('error', 'internal server error'), 500