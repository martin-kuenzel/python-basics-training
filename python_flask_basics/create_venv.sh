#!/bin/bash

python3 -m venv flask_project &&\
source flask_project/bin/activate &&\
pip install flask &&\
pip freeze > requirements.txt &&\
export FLASK_APP=flask_blog.py &&\
deactivate &&\
exit 0

exit 1