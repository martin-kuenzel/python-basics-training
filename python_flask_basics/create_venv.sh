#!/bin/bash

python3 -m venv flask_project &&\

(cat <<ENV_ADD

export SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(16));')
export FLASK_APP=run.py

ENV_ADD
) >> flask_project/bin/activate &&\

source flask_project/bin/activate &&\
pip install flask &&\
pip install flask-wtf &&\
pip install flask-sqlalchemy &&\
pip install flask-bcrypt &&\
pip install flask-login &&\
pip freeze > requirements.txt &&\
deactivate &&\
exit 0

exit 1