from machine import Pin, PWM
import time
from mfrc522_i2c import mfrc522

#Define GPIO15’s output frequency as 50Hz and assign them to PWM.
servoPin = Pin(15)
pwm = PWM(servoPin, freq=50)

#i2c config
addr = 0x28
scl = 22
sda = 21
    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()
rc522.ShowReaderDetails()            # Show details of PCD - MFRC522 Card Reader details

uid1 = [147, 173, 247, 32]
uid2 = [57, 182, 70, 194]

pwm = PWM(servoPin, freq=50)
pwm.duty(128)
time.sleep(1)

while True:
    if rc522.PICC_IsNewCardPresent():
        #print("Is new card present!")
        if rc522.PICC_ReadCardSerial() == True:
            print("Card UID:", end=' ')
            print(rc522.uid.uidByte[0 : rc522.uid.size])
            if rc522.uid.uidByte[0 : rc522.uid.size] == uid1 or rc522.uid.uidByte[0 : rc522.uid.size] == uid2:
                pwm = PWM(servoPin, freq=50)
                pwm.duty(25)
            else :
                pwm = PWM(servoPin, freq=50)
                pwm.duty(128)
            time.sleep(500)