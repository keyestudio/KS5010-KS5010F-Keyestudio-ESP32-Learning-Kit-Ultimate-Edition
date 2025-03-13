from machine import Pin
import time

motor1a = Pin(15, Pin.OUT) # create motor1a object from Pin 15, Set Pin 15 to output
motor1b = Pin(2, Pin.OUT) # create motor1b object from Pin 2, Set Pin 2 to output

def forward():
    motor1a.value(1) # Set motor1a high
    motor1b.value(0) # Set motor1b low
def backward():
    motor1a.value(0)
    motor1b.value(1)
def stop():
    motor1a.value(0)
    motor1b.value(0)

def test():
    forward() # motor forward
    time.sleep(5) #delay
    stop() # motor stop
    time.sleep(2)
    backward()# motor backward 
    time.sleep(5)
    stop()
    time.sleep(2)
    
for i in range(5):
    test() 