from flask import Flask, request, abort
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# notes: i want to create a filesystem here
# i need a database connection, and a database for that matter
# routes:
# list(page, offset)
# search(page, offset, params)
# post(puzzledata)
# put(puzzledata) for warning on a puzzle, which should email me.
# health/availability
# so... i need a database next.
# 
# script setup
# server.py
# tools/
#   db.py 
#   constants.py
#   puzzle_list.py < for processing search requests, page logic etc
#   email.py < for connecting to smtp server
# setup/
#   install.py < flask, mariadb
#   create_tables.sql

# what else don't i know?
# how to connect to a db
# how to connect to smtp
# wsgi, what it is, how it integrates with apache web server

app = Flask(__name__)

@app.get("/picresse/list")
def list():
    page_size = request.args.get('page')
    offset = request.args.get('offset')
    if (page_size == None or offset == None):
        abort(400)
    return [{'id': 1, 'asdf': 'fdsa'}]
    
@app.get("/picresse/search")
def search():
    page_size = request.args.get('page')
    offset = request.args.get('offset')
    if (page_size == None or offset == None):
        abort(400)
    #todo: add search param filter
    return [{'id': 1, 'asdf': 'fdsa'}]

@app.get("/debug/<str>")
def debug(str):
    app.logger.info("% have triggered the debug state", str)
    return 'debug'

#TODO: database health
@app.get("/health")
def health():
    return 'OK'

@app.get("/availability")
def availability():
    return 'OK'

@app.route("/nongetcheck/<str>", methods=['POST', 'PUT'])
def nongetcheck(str):
    return '%s OK' % str