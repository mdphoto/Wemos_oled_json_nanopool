# -*- coding: utf-8 -*-

from umqtt.simple import MQTTClient
import utime
import ssd1306
import ure
import urequests
from machine import I2C, Pin

def sub_cb(topic, msg):
    print((topic, msg))

# Affichage oled
    i2c = I2C(sda=Pin(4), scl=Pin(5))
    display = ssd1306.SSD1306_I2C(64, 48, i2c)
    display.fill(0)
    display.text('{0}'.format(msg), 0, 0)
    display.text("Je roule", 0, 20)
    display.show()

# Connexion à mosquitto
c = MQTTClient("umqtt_client", "192.168.1.181",port=1883)
c.set_callback(sub_cb)
c.connect()
c.subscribe("/Aqua-core-001/DHT22/Temperature")

while True:
    c.check_msg()
    utime.sleep(0.5)
