#!/bin/sh

# This sets up a new virtual environment
mkvirtualenv -p /usr/bin/python2.7 doorbell
workon doorbell
pip install -r requirments.txt
pip install -e .
mv doorbell/settings.json.example doorbell/settings.json
