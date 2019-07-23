#!/bin/bash

python3 -m venv flask_project &&\
source flask_project/bin/activate &&\
pip install flask &&\
pip install flask-wtf &&\
pip freeze > requirements.txt &&\
deactivate &&\
exit 0

exit 1