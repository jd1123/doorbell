from doorbell import app
from flask import render_template, redirect, request, url_for, jsonify
import doorbell.config

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if (len(request.form.keys()) == 0) or ('pw' not in request.form.keys()):
        supplied_pw = ''
    else:
        supplied_pw = request.form['pw']

    print request.form.keys()
    if supplied_pw == app.config['settings']['authPassword']:
        token = doorbell.config.new_token()
        app.config['registered_clients'].append(token)
        return token 
    else:
        token = doorbell.config.new_token()
        app.config['registered_clients'].append(token)
        print app.config['registered_clients']
        return token
        return "403: Forbidden", 403


class InvalidPassword(Exception):
    status_code = 403
    
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidPassword)
def handle_invalid_password(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

