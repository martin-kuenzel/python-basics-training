#!/bin/bash

python3 -m venv project_env &&\
source project_env/bin/activate &&\
pip install requests &&\
pip install pytz &&\
pip freeze > requirements.txt &&\
deactivate &&\
exit 0

exit 1