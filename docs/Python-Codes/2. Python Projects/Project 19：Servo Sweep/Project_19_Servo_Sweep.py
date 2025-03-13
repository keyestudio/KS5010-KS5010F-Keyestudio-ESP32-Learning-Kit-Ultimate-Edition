from myservo import myServo #Import myservo module.
import time

#Initialize pins of the servo and set the starting point of the servo to 0 degree.
servo=myServo(15)
servo.myServoWriteAngle(0)
time.sleep_ms(1000)

try:
    while True:
#Use two for loops. The first one controls the servo to rotate from 0 degree to 180 degrees
#while the other controls it to rotate back from 180 degrees to 0 degree.
        for i in range(0,180,1):
            servo.myServoWriteAngle(i) #Control the servo to rotate to a specified angle within the range of 0-180 degrees.
            time.sleep_ms(15)
        for i in range(180,0,-1):
            servo.myServoWriteAngle(i)
            time.sleep_ms(15)        
except:
    servo.deinit()