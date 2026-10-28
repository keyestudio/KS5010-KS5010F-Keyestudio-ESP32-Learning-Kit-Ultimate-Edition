from machine import Pin
import time

led = Pin(15, Pin.OUT)   # create LED object from Pin 15, Set Pin 15 to output

led.value(1)    # Set led turn on

