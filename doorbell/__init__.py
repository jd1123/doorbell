from flask import Flask
app = Flask(__name__, static_url_path='/static')

import doorbell.views
import doorbell.config

configdat = doorbell.config.readconfig()
creddat = doorbell.config.readcred()
timeconfig = doorbell.config.readtimeconfig()
app.config['main_config'] = configdat
app.config['settings'] = creddat
app.config['time_config'] = timeconfig
app.config['registered_clients'] = []

#app.config['ring'] = configdat['ring']
#app.config['sendtext'] = configdat['sendtext']
#app.config['gmailLogin'] = creddat['gmailLogin']
#app.config['gmailPassword'] = creddat['gmailPassword']
#app.config['toNumbers'] = creddat['toNumbers']
#app.config['soundTimerEnabled'] = timeconfig['soundEnabled'] 
#app.config['textTimerEnabled'] = timeconfig['textEnabled']
#app.config['textTimeStart'] = timeconfig['textConfig']['startTime'] 
#app.config['textTimeEnd'] = timeconfig['textConfig']['endTime'] 
#app.config['soundTimeStart'] = timeconfig['soundConfig']['startTime'] 
#app.config['soundTimeEnd'] = timeconfig['soundConfig']['endTime'] 
