# Import keypad module.
from keypad import KeyPad
import time
# Associate the keypad module to ESP32 pins. 
keyPad = KeyPad(22, 21, 19, 18, 17, 16, 4, 0)
#Call function keyPan.scan() to obtain the value of the pressed key. Once it is obtained, print it out. 
def key():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print(keyvalue, end="\t")
        time.sleep_ms(300)
        return keyvalue
            
while True:
    key()
