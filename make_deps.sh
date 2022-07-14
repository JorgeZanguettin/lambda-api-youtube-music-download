#!/bin/bash

/usr/bin/python3.8 -m virtualenv temp_venv
source temp_venv/bin/activate
pip install -r requirements.txt
cp -R lambda_function.py /usr/lib/x86_84-linux-gnu/libpq.so.5 temp_venv/lib/python3.8/site-packages/
cd temp_venv/lib/python3.8/site-packages/
zip -r lambda_function.zip *
cd -
cp temp_venv/lib/python3.8/site-packages/lambda_function.zip .
deactivate
rm -R temp_venv
