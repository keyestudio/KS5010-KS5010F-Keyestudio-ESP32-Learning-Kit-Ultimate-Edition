from machine import ADC, Pin
import time
 
# Turn on and configure the ADC with the range of 0-3.3V 
adc=ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
 
# Pin initialization
motor1a = Pin(15, Pin.OUT) # create motor1a object from Pin 15, Set Pin 15 to output
motor1b = Pin(2, Pin.OUT) # create motor1b object from Pin 2, Set Pin 2 to output

# If the Sound sensor detects Sounds, and the motor will rotate
# when the analog value is greater than 600,Otherwise, the motor does not rotate.    
while True:
    adcVal=adc.read()
    print(adcVal)
    time.sleep(0.5)
    if adcVal >600:
        motor1a.value(1) # Set motor1a high
        motor1b.value(0) # Set motor1b low
        time.sleep(5)   # delay time 
    else:
        motor1a.value(0)
        motor1b.value(0)