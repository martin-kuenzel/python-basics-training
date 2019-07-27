#!/bin/bash

echo "changing to directory $(realpath $(dirname $0))"

cd $(realpath $(dirname $0))

[ -e ./flask_project ] && { echo "./flask_project already exists ... removing first ..." && rm -rf ./flask_project; }

python3 -m venv flask_project &&\

read -s -p $'\ngive me an email address:' EMAIL_ACCOUNT &&\
read -s -p $'\ngive me a password:' EMAIL_PASSWORD &&\

(cat <<ENV_ADD

export SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(16));')
export FLASK_APP=run.py
export EMAIL_ACCOUNT=$EMAIL_ACCOUNT
export EMAIL_PASSWORD=$EMAIL_PASSWORD
export SQLALCHEMY_DATABASE_URI="sqlite:///site.db"

ENV_ADD
) >> flask_project/bin/activate &&\
sed -i 's/deactivate () {/deactivate () {\nunset SECRET_KEY FLASK_APP EMAIL PASSWORD/' flask_project/bin/activate &&\
source flask_project/bin/activate &&\
pip install flask &&\
pip install flask-wtf &&\
pip install flask-sqlalchemy &&\
pip install flask-bcrypt &&\
pip install flask-login &&\
pip install Pillow &&\
pip install flask-mail &&\
pip install -U flask-paginate &&\
pip freeze > requirements.txt &&\
deactivate &&\
echo -e "-- Setup completed --\nTo activate the virtual environment run:\nsource flask_project/bin/activate" &&\
exit 0

exit 1