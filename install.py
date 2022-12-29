import subprocess
import sys

db_params = {
    "user": "hazashami",
    "password": "",
    "host": "localhost",
    "database": "picresse"
}

#need to make the actual database
table_scripts = [
    """CREATE TABLE t_puzzles ( 
        c_id INTEGER AUTO_INCREMENT, 
        c_name VARCHAR(255) NOT NULL,
        c_creator VARCHAR(255) NOT NULL, 
        c_width INTEGER NOT NULL,
        c_length INTEGER NOT NULL,
        c_puzzle VARCHAR(255) NOT NULL,
        c_date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
        c_date_updated DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
        c_date_deleted DATETIME NULL,
        c_is_warned BOOLEAN NOT NULL DEFAULT 0,
        c_times_completed INTEGER NULL
        );"""
]

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip' 'install', package])

def create_tables(password):
    db_params["password"] = password
    connection = mariadb.connect(**db_params)
    #if bad connection exit and warn!!!
    db_params["password"] = ""
    cursor = connection.cursor()
    for script in table_scripts:
        cursor.execute(script)

try:
    import flask
except ImportError:
    install('flask')

try:
    import mariadb
except ImportError:
    install('mariadb')

if len( sys.argv > 2 and sys.argv[1] is '--create-tables'):
    create_tables(sys.argv[2])