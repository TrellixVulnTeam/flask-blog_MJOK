from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
import sqlite3

DATABASE = 'blog.db'

app = flask(__name__)

app.config.from__object(__name__)

def connectdb():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == __main__:
    app.run(debug=True)
