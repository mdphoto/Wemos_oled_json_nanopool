# -*- coding: utf-8 -*-
import urequests
import utime
import ssd1306
import ure
from machine import I2C, Pin

def pull_aqua():
    """Import aqua_core-001 json"""
    url = urequests.get('http://192.168.1.38/json').json()
    aqua = url['Sensors'][0]['Temperature']
    return aqua

def pull_xmr_hashrate():
    """Import XMR json on nanopool"""
    url = urequests.get('https://api.nanopool.org/v1/xmr/user/46GuwN97BtL2pikZyjb9Aj8fDBAitvNN3St9wW4L1UuNYZn1pYjBUwXWbwaVe4vUMveKAzAiA4j8xgUi29TpKXpm3ybbnEM').json()
    hashrate = url['data']['hashrate']
    return hashrate

def pull_xmr_balance():
    """Import XMR json on nanopool"""
    url = urequests.get('https://api.nanopool.org/v1/xmr/user/46GuwN97BtL2pikZyjb9Aj8fDBAitvNN3St9wW4L1UuNYZn1pYjBUwXWbwaVe4vUMveKAzAiA4j8xgUi29TpKXpm3ybbnEM').json()
    balance = url['data']['balance']
    return balance

while True:
    balance = pull_xmr_balance()
    hashrate = pull_xmr_hashrate()
    temp = pull_aqua()
# Affichage oled
    i2c = I2C(sda=Pin(4), scl=Pin(5))
    display = ssd1306.SSD1306_I2C(64, 48, i2c)
    display.fill(0)
    display.text('Tmp:', 0, 0)
    display.text('{0}'.format(temp), 32, 0)
    display.text('{0}'.format(balance), 0, 20)
    display.text('{0}'.format(hashrate), 10, 40)
    display.show()
    utime.sleep(60)
