import sqlite3
from flask import current_app, g

def get_db(database_name):
    if 'db' not in g:
        if (database_name == 'leaderboard'):
            g.db = sqlite3.connect('app/data/leaderboard.db')
        elif (database_name == 'test'):
            g.db = sqlite3.connect('app/data/test.db')
        else:
            print('Invalid database name');
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(database_name):
    db = get_db(database_name)
    # Execute the schema.sql file to initialize the database schema
    with current_app.open_resource('data/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()
