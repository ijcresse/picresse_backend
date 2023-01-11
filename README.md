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

### first time setup (on hazasha.me, using apache2, debian10)
#### this is more for me than anyone else
```
cd /var/www/html
git clone picresse_backend
python3 -m pip install -r requirements.txt
# may require installing mariadb and/or mariadb connector/c

# setup mod-wsgi on the apache2 server. installation performed on debian 10
sudo apt-get install libapache2-mod-wsgi -y
systemctl restart apache2
touch /etc/apache2/conf-available/mod-wsgi.conf
#add in the following contents:
WSGIScriptAlias /picresse /var/www/html/picresse/wsgi.py
#save and close

#may need to run this as root
a2enconf mod-wsgi
systemctl restart apache2

#back in picresse folder
mod_wsgi-express start-server wsgi.py --processes 1
```
verify serving python content via apache2 by accessing <site>:<port>/health

### repeated deployments
```
cd /var/www/html/picresse_backend
git pull
# in case of any new requirements!
pythom3 -m pip install -r requirements.txt
systemctl restart apache2
screen -r picresse
mod_wsgi-express start-server wsgi.py --processes 1
```
verify /health endpoint