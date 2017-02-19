/* 
	Doorbell sketch for NodeMCU ESP-12E using the
	Arduino IDE: http://arduino.esp8266.com/stable/package_esp8266com_index.json
	Please edit the globals with your own values.
*/

#include <ESP8266WiFi.h>
// GLOBAL CONFIG 
const char* ssid = "SSID";				// wifi ssid
const char* password = "SSIDPassword";	// wifi password
const char* host = "HOST";				// host for http doorbell service
const String url = "/ring";				// the "ring" URI
const int httpPort = 5000;				// service port
// END GLOBAL CONFIG

const int buttonPin = 5;				// Button input pin
const int ledPin = 16;					// led pin (16 is onboard led)
int buttonState = 0;

/* 
   This connects to the wifi network
*/
void connectWifi(){
	Serial.println();
	Serial.println();
	Serial.print("Connecting to LAN: ");
	Serial.println(ssid);

	WiFi.begin(ssid, password);
	
	while (WiFi.status() != WL_CONNECTED){
		delay(500);
		Serial.print(".");
	}
	
	Serial.println("");
	Serial.println("Wifi Connected!");
	Serial.println("IP Address: ");
	Serial.println(WiFi.localIP());
}


/* 
   This rings the doorbell with
   a HTTP request 
*/
void hitHost(){
	Serial.print("Connecting to: ");
	Serial.println(host);

	WiFiClient client;
	
	if(!client.connect(host, httpPort)){
		Serial.println("Connection failed");
		return;
	}
	
	Serial.print("Request URL: ");
	Serial.println(url);

	client.print(String("Get ") + url + " HTTP/1.1\r\n" +
				 "Host: " + host + "\r\n" +
				 "Connection: close\r\n\r\n");

	delay(500);

	while(client.available()){
		String line = client.readStringUntil('\r');
		Serial.print(line);
	}

	Serial.println();
	Serial.println("Closing connection");
	delay(2000);
}

/*
   Various setup - pin in and out and serial
   communication
*/
void setup(){
	Serial.begin(115200);

	pinMode(buttonPin, INPUT_PULLUP);
	pinMode(ledPin, OUTPUT);
	WiFi.mode(WIFI_STA);
	delay(100);
	connectWifi();
}

/* 
   Main microcontroller loop
   listens for button pushes and rings
   the web server
*/
void loop(){
	buttonState=digitalRead(buttonPin);

	if(buttonState == LOW){
		digitalWrite(ledPin, LOW);
		hitHost();
	} else {
		digitalWrite(ledPin, HIGH);
	}
}
