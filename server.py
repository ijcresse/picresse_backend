#main script. coordinates routes and passes functionality to helper functions.

from flask import Flask, request, abort
from logging.config import dictConfig
import json
import sys

from tools import db, puzzle_reader

file = open('./tools/constants.json')
data = json.load(file)
dictConfig(data['dictconfig'])

# TODO:
#   email.py < for connecting to smtp server
# what else don't i know?
# how to connect to smtp
# wsgi, what it is, how it integrates with apache web server

app = Flask(__name__)
app.config.from_prefixed_env()
if (app.config["DB_USER"] == None or app.config["DB_PASS"] == None):
    raise ValueError("No DB_USER or DB_PASS set for Flask application")
else:
    print("environment variables detected, starting up", file=sys.stdout)
    db_user = app.config["DB_USER"]
    db_pass = app.config["DB_PASS"]

if (app.config["ENV"] == 'production'):
    print("starting production version of server!")

@app.get("/picresse/puzzle/list")
def list():
    page_size = request.args.get('page')
    offset = request.args.get('offset')

    if (page_size == None or offset == None):
        abort(400)

    try:
        c = db.get_db_connection(db_user, db_pass)
    except:
        abort(500, description = "ERROR: database connection not available")
    
    try:
        rows = db.get_list(page_size, offset, c)
        db.close_db_connection(c)
    except Exception as e:
        abort(400, description = str(e))

    return [{'list': rows}]
    
#TODO: get all search params?
@app.get("/picresse/puzzle/search")
def search():
    page_size = request.args.get('page')
    offset = request.args.get('offset')
    # puzzle[]=a&puzzle[]=b&puzzle[]=c OR puzzle=a&puzzle=b&puzzle=c, application/x-www-form-urlencoded
    puzzle = request.args.getlist('puzzle')

    if (page_size == None or offset == None):
        abort(400)
    
    try:
        c = db.get_db_connection(db_user, db_pass)
    except:
        abort(500, description = "ERROR: database connection not available")

    try:
        rows = db.search_list(puzzle_reader.search_params(puzzle), page_size, offset, c)
        db.close_db_connection(c)
    except Exception as e:
        abort(400, description = str(e))

    return [{'list': rows}]

@app.post("/picresse/puzzle/create")
def create():
    puzzle = request.get_json()
    
    try:
        c = db.get_db_connection(db_user, db_pass)
    except:
        abort(500, description = "ERROR: database connection not available")

    try:
        db.post_puzzle(puzzle, c)
        db.close_db_connection(c)
    except Exception as e:
        abort(400, description = str(e))
    return "OK", 204
    

@app.get("/health")
def health():
    try:
        c = db.get_db_connection(db_user, db_pass)
        db.close_db_connection(c)
    except:
        return "DB DOWN", 500
    return "OK", 200

@app.get("/availability")
def availability():
    return {"status": 200, "message": "OK"}