import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# get database object for response
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# close database connection at the end of response
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# reset and initialize database 
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# create a flask command 'init-db' 
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# function that registers the database with Flask object
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)