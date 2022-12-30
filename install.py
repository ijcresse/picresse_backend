import subprocess
import sys
import json

file = open('./tools/constants.json')
data = json.load(file)
db_params = data['db_params']
table_script = data['table_scripts'][0]

def install(package):
    print('installing %s' % package)
    subprocess.check_call([sys.executable, '-m', 'pip' 'install', package])

def create_tables(user, password):
    db_params["user"] = user
    db_params["password"] = password
    connection = mariadb.connect(**db_params)
    #if bad connection exit and warn!!!
    db_params["password"] = ""
    cursor = connection.cursor()
    cursor.execute(table_script)

try:
    import flask
except ImportError:
    install('flask')

try:
    import mariadb
except ImportError:
    install('mariadb')

if len(sys.argv) > 3 and sys.argv[1] == '--create-tables':
    create_tables(sys.argv[2], sys.argv[3])
else:
    print('"--create-tables <user> <password>" not specified, skipping table creation')