#!/usr/bin/env bash

python3 -m venv --clear --copies ./venv
source ./venv/bin/activate
python3 ./meter.py
