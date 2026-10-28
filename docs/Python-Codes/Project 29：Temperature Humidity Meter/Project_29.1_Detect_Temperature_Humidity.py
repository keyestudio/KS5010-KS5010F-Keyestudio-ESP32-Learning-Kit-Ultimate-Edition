# Import machine, time and dht modules. 
import machine
import time
import dht

#Associate DHT11 with Pin(13).
DHT = dht.DHT11(machine.Pin(13))

# Obtain temperature and humidity data once per second and print them out. 
while True:
    DHT.measure() # Start DHT11 to measure data once.
   # Call the built-in function of DHT to obtain temperature
   # and humidity data and print them in “Shell”.
    print('temperature:',DHT.temperature(),'℃','humidity:',DHT.humidity(),'%')
    time.sleep_ms(1000)