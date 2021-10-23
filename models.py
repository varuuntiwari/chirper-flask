import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('INSERT INTO posts (name, chirp) VALUES (?, ?)', (name, content))
    conn.commit()
    conn.close()

def get_posts():
    conn = sql.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('SELECT * FROM posts')
    chirps = cur.fetchall()
    return chirps