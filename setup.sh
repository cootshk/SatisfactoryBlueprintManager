#!/bin/bash
cd $0
python3 -m venv venv
. /venv/Scripts/activate
python3 -m pip install -e .