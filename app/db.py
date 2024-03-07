import sqlite3
from flask import app, g

def get_db():
    if 'db' not in g:
        # Adjust the path according to your `schema.sql` location
        g.db = sqlite3.connect(app.config['data/schema.sql'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()
    # Adjust the path to where your `schema.sql` file is located
    with app.open_resource('data/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    db.commit()
