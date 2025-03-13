# Import the infrared decoder.
from irrecvdata import irGetCMD

# Associate the infrared decoder with GP0.
recvPin = irGetCMD(0)

#When infrared key value is obtained, print it out in"Shell". 
try:
    while True:
        irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.
        if irValue:
            print(irValue)
except:
    pass