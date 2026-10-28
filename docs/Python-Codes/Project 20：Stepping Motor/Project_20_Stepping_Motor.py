from machine import Pin
import time
 
# Pin initialization
in1 = Pin(15, Pin.OUT)
in2 = Pin(16, Pin.OUT)
in3 = Pin(17, Pin.OUT)
in4 = Pin(18, Pin.OUT)
 
# Delay time
delay = 1
 
# The number of steps required for the motor to rotate one revolution, (about 360°), with a slight deviation
ROUND_VALUE = 509
 
# The sequence value of the four-phase eight-beat stepper motor: A-AB-B-BC-C-CD-D-DA-A。
STEP_VALUE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]
 
# Pin output low level
def reset():
    in1(0)
    in2(0)
    in3(0)
    in4(0)
 
# If count is positive integers turn clockwise, if count is negative integers turn counterclockwise
def step_run(count):
    direction = 1     # turn clockwise
    if count < 0:
        direction = -1  # turn counterclockwise
        count = -count
    for x in range(count):
        for bit in STEP_VALUE[::direction]:
            in1(bit[0])
            in2(bit[1])
            in3(bit[2])
            in4(bit[3])
            time.sleep_ms(delay)
    reset()
 
# If a is positive integers turn clockwise, if a is negative integers turn counterclockwise
def step_angle(a):
    step_run(int(ROUND_VALUE * a / 360))
 
# Cycle: turn clockwise one circle, then counterclockwise one circle.
while True:
    step_run(509)
    step_run(-509)
    step_angle(360)
    step_angle(-360)