# Picresse Backend Setup
A Flask REST API for serving basic functionality for user-generated puzzles for the Picresse game.

## install guide
Set up requirements
`pip install -r requirements.txt`
Setup a mariaDB database called 'picresse'.
Run the tools/install.py script, which will create a table in the picresse database.
`python install.py --create-tables <user> <password>`

## run guide
### dev run
```
export FLASK_DB_USER=user
export FLASK_DB_PASS=pass
export FLASK_ENV=development
python -m flask --app server --debug run
```

### prod run (on existing apache web server)
```
screen -S picresse_server
#head to the root page for apache web server
cd /var/www/html
sudo git clone picresse_backend
cd picresse_backend

#setup virtual python environment
python -m venv picresse_env
source/picresse_env/activate
#verify python env
which python

#install dependencies
pip install -r requirements.txt

export FLASK_DB_USER=user
export FLASK_DB_USER=pass
export FLASK_ENV=production

#verify dev server works
python -m flask --app server --debug run

#configure wsgi file
cp tools/site.wsgi ./picresse_site.wsgi

```

