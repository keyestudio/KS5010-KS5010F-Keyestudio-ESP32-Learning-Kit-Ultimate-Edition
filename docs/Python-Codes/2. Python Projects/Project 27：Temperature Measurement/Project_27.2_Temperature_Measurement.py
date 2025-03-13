from machine import ADC, Pin
import time

# Turn on and configure the ADC with the range of 0-3.3V 
adc=ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
conversion_factor = 3.3 / (4095)

# create red led object from Pin 15, Set Pin 15 to output
led_red = Pin(15, Pin.OUT)  
# create yellow led object from Pin 2, Set Pin 2 to output
led_yellow = Pin(2, Pin.OUT)
# create green led object from Pin 4, Set Pin 4 to output
led_green = Pin(4, Pin.OUT) 

while True:
    adcVal=adc.read()
    reading = adcVal * conversion_factor 
    temperature = reading * 102.4 
    print(temperature)
    time.sleep(0.2)
    if temperature <20:
        led_red.value(1)  # Set red led turn on
        led_yellow.value(0) # Set yellow led turn off 
        led_green.value(0)  # Set green led turn off
    elif temperature >=20 and temperature <25:
        led_red.value(0)  # Set red led turn off
        led_yellow.value(1) # Set yellow led turn on 
        led_green.value(0)  # Set green led turn off
    else:
        led_red.value(0)  # Set red led turn off
        led_yellow.value(0) # Set yellow led turn off 
        led_green.value(1)  # Set green led turn on