from myservo import myServo #Import myservo module.
from keypad import KeyPad
from machine import Pin
import time

keyPad = KeyPad(22, 21, 19, 18, 17, 16, 4, 0)
servo=myServo(15)
servo.myServoWriteAngle(0)
time.sleep_ms(1000)
activeBuzzer = Pin(2, Pin.OUT)

# Define an array and set the password. 
passWord = "1234"
keyIn = ""
def key():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print('Your input:', keyvalue)
        time.sleep_ms(200)
        return keyvalue

while True:
 # Each time a key is pressed, the buzzer will short beep once,
 # and the key value of the key will be stored in the keyIn array. 
    keydata = key()
    if keydata != None:
        activeBuzzer.value(1)
        time.sleep_ms(100)
        activeBuzzer.value(0)
        keyIn += keydata 
# When 4 keys are pressed, it will judge whether the password is correct.
# If it is correct, the servo will rotate 90 degrees, and then turn back after 1 second.
# If the password is wrong, the buzzer will long beep once and the keyInNum value will be cleared.        
    if len(keyIn) == 4:
        if keyIn == passWord:
            print("passWord right!")
            servo.myServoWriteAngle(90)
            time.sleep_ms(1000)
            servo.myServoWriteAngle(0)
        else:
            print("passWord error!")
            activeBuzzer.value(1)
            time.sleep_ms(1000)
            activeBuzzer.value(0)
        keyIn = ""