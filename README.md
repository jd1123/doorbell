# A Home Made Wifi Doorbell

## Why?
You could buy a Ring for $199-$249, but then you not only have to trust the company that sells it, but also have some sort of security in place. Doorbell is completely open source (even hardware if you opt for an open alternative to the raspberry pi). Tinker with it yourself. Know what's happening. Trust no one.

## Requirements:

### Hardware:
* A NodeMCU microcontroller
* A computer to host the web app on (a raspberry pi or something similar)
* A doorbell or other button to trigger a ring

### Software:
* Python 2.7
* Flask
* Arduino IDE

## The system
This is a very basic doorbell system. The NodeMCU is connected to a doorbell (a button). When the circut is closed, the NodeMCU sends an HTTP request to a web app hosted on your local network, for example a raspberry pi. The raspberry pi then plays a sound, sends a text message or both. You can configure the behavior from the root uri of the web app.

This projects includes an Arduino sketch for the NodeMCU and a webapp to interpret the http requests. The webapp is written with flask.

## Layout
Here is a layout of the basic circuit. You can replace the 9v battery with any power source: 

![Image of Schematic]
(https://github.com/jd1123/doorbell/blob/master/DoorbellSchematic_bb.png)

## Get going:
1. Set up a computer to host the webapp on and **set a static ip address for it.**
2. Set up the NodeMCU microcontroller:
	* Change the wifi credentials in the NodeMCU sketch to your own.
	* Change the host to the static ip you set for your hosting computer. 
	* Enter your gmail credentials into settings.json in the webapp.
	* Set the correct email address you would like to recieve emails at when someone rings your doorbell. I set it up so that it send my wife a text message ([SMS gateways](https://en.wikipedia.org/wiki/SMS_gateway)).
	* Enable [less secure applications](https://support.google.com/accounts/answer/6010255?hl=en) for your gmail account. I would create a new gmail to send these messages.
3. Get a 3d printed case for the microcontroller.
4. Hook up your existing doorbell (or run wires for a new one) to pins D1 and GND.
5. Plug in the controller to a wall outlet using a micro USB cable.
6. Enjoy. 

## Some notes:

* You may want an enclosure to house your NodeMCU so you can mount it. [Here](https://www.thingiverse.com/thing:1128026) is a link to one. Other options are available.
* The sound file in the sounds/ directory is attributable to [Sound Jay](https://www.soundjay.com/tos.html) and used with his express permission.
