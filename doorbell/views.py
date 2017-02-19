from doorbell import app
import subprocess
import os
from flask import render_template, redirect, request, url_for, jsonify
import doorbell.config
import doorbell.sendemail
import datetime

@app.route('/', methods=['GET', 'POST'])
def root_route():
    cdict = app.config['time_config']
    if request.method == 'GET':
        ring = app.config['main_config']['ring']
        sendtext = app.config['main_config']['sendtext']
        return render_template('index.html', ring=ring, sendtext=sendtext, cdict = cdict, updtmsg=False)
    elif request.method == 'POST':
        print request.form
        sound_timer_enabled = False
        text_timer_enabled = False
        ring = doorbell.config.str2bool(request.form['ring'])
        sendtext = doorbell.config.str2bool(request.form['sendtext'])
        doorbell.config.writeconfig(ring, sendtext)
        
        if ('soundTimerEnabled' in request.form.keys()):
            sound_timer_enabled = True
        if ('textTimerEnabled' in request.form.keys()):
            text_timer_enabled = True
        
        doorbell.config.write_timeconfig(sound_timer_enabled, text_timer_enabled)
        
        # update global config
        app.config['main_config']['ring'] = ring
        app.config['main_config']['sendtext'] = sendtext
        app.config['time_config']['soundEnabled'] = sound_timer_enabled
        app.config['time_config']['textEnabled'] = text_timer_enabled
        
        return render_template('index.html', ring=ring, sendtext=sendtext, cdict = cdict, updtmsg=True)

@app.route('/ring', methods=['GET', 'POST'])
def ring():
    remote_ip = request.remote_addr
    print 'Request from: ' + remote_ip
    response_text = "ding dong"

    fpath = os.path.join(os.getcwd(), 'sounds', 'doorbell-2.mp3')
    ring_bell = app.config['main_config']['ring']
    send_text = app.config['main_config']['sendtext']
    dtnow = datetime.datetime.now().time()

    if app.config['time_config']['soundEnabled']:
        stTime = datetime.time(app.config['time_config']['soundTimeStart'][0], app.config['time_config']['soundTimeStart'][1], 0)
        endTime = datetime.time(app.config['time_config']['soundTimeEnd'][0], app.config['time_config']['soundTimeEnd'][1], 0)
        if (dtnow < stTime) or (dtnow > endTime):
            ring_bell = False
            response_text = response_text + " - ring disabled by timer"
    
    if app.config['time_config']['textEnabled']:
        stTime = datetime.time(app.config['time_config']['textTimeStart'][0], app.config['time_config']['textTimeStart'][1], 0)
        endTime = datetime.time(app.config['time_config']['textTimeEnd'][0], app.config['time_config']['textTimeEnd'][1], 0)
        if (dtnow < stTime) or (dtnow > endTime):
            send_text = False
            response_text = response_text + " - text disabled by timer"

    if ring_bell == True:
        subprocess.Popen(['mpg123', '-q', fpath])

    if send_text == True:
        doorbell.sendemail.send_email(remote_ip)
    
    return response_text

