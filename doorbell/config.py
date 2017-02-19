import json
from uuid import uuid4

def readconfig():
    with open('doorbell/config/config.json', 'r') as f:
        data = json.load(f)
    return data

def readcred():
    with open('doorbell/config/settings.json', 'r') as f:
        data = json.load(f)
    return data

def readtimeconfig():
    with open('doorbell/config/timeconfig.json', 'r') as f:
        data = json.load(f)
    return data

def writeconfig(ring, sendtext):
    cdict = dict()
    cdict['ring'] = ring
    cdict['sendtext'] = sendtext

    if (not (check_type(ring) and check_type(sendtext)) ):
        return False

    with open('doorbell/config/config.json', 'w') as f:
        json.dump(cdict, f)

    return True

def write_timeconfig(sound_timer_enabled, text_timer_enabled):
    cdict = readtimeconfig()
    
    if (not (check_type(sound_timer_enabled) and check_type(text_timer_enabled)) ):
        return False
    
    cdict['soundEnabled'] = sound_timer_enabled
    cdict['textEnabled'] = text_timer_enabled
    
    with open('doorbell/config/timeconfig.json', 'w') as f:
        json.dump(cdict, f)


def check_type(v):
    if (isinstance(v, (bool)) ):
        return True
    else:
        return False

def str2bool(s):
    return s.lower() in ("yes", "true", "t", "1")

def new_token():
    return ''.join(str(uuid4()).split('-'))

