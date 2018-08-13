import MySQLdb
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import time

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)


def connect_db():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    cur = conn.cursor()
    conn.select_db('test')
    return cur


@app.before_request
def before_request():
    g.conn = MySQLdb.connect(host='localhost', user='root', passwd='', port=3306)
    g.db = g.conn.cursor()
    g.conn.select_db('test')


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] is None:
            error = 'Invalid username'
        else:
            session['logged_in'] = True
            session['name'] = request.form['username']
            flash('You are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('show_entries'))


@app.route('/')
def show_entries():
    g.db.execute('select name,text,time from entries order by id desc')
    entries = [dict(name=row[0], text=row[1], time=row[2]) for row in g.db.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    g.db.execute('insert into entries(name,text,time) values(%s,%s,%s)',
                 [request.form['name'], request.form['text'], current_time])
    g.conn.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


if __name__ == "__main__":
    app.run()
