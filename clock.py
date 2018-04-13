#!/usr/bin/python3

import time
from sense_hat import SenseHat

sense = SenseHat()
showSensorInterval = 60

showSensorInterval = showSensorInterval / 4


def auto_rotate_display():
    # read sensors data to detect orientation
    x = round(sense.get_accelerometer_raw()['x'], 0)
    y = round(sense.get_accelerometer_raw()['y'], 0)
    rot = 0
    if x == -1:
        rot = 90
    elif y == -1:
        rot = 180
    elif x == 1:
        rot = 270
    sense.set_rotation(rot)


def showSensorData():
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    # pressure = sense.get_pressure()
    # sense.show_message("%.1fhPa " % pressure, scroll_speed=0.10, text_colour=[0, 50, 0])
    sense.show_message("%.1fC " % temp, scroll_speed=0.10, text_colour=[0, 50, 0])
    sense.show_message("%.1f%%" % humidity, scroll_speed=0.10, text_colour=[0, 0, 50])


def showTime() -> object:
    hour = str(time.localtime().tm_hour)
    minute = time.localtime().tm_min

    if minute < 10:
        zero = "0"
    else:
        zero = ""

    minute = str(minute)

    # Display the time
    sense.low_light = True  # Optional
    # sense.set_rotation(90) # Optional
    sense.show_message(hour + ":" + zero + minute, scroll_speed=0.10, text_colour=[50, 0, 0])


while True:

    timeWait = 0
    while timeWait <= showSensorInterval:
        auto_rotate_display()
        showTime()
        time.sleep(1)
        timeWait += 1

    showSensorData()
