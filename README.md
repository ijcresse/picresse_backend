# Picresse Backend Setup
A Flask REST API for serving basic functionality for user-generated puzzles for the Picresse game.

## install guide
Set up MariaDB and create a database called 'picresse'.
Run install.py
`python install.py --create-tables <user> <password>`
This will install flask, mariadb for python, and create the prerequisite table.

## run guide
something something wsgi apache web server???
### dev run
```
export FLASK_DB_USER=user
export FLASK_DB_PASS=pass
export FLASK_ENV=development
python -m flask --app server --debug run
```

need to figure out run args for prod.
```
export FLASK_DB_USER=user
export FLASK_DB_USER=pass
export FLASK_ENV=production
```

