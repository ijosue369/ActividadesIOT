from gpiozero import LED, Button
from time import sleep
 
ledR = LED(13)
ledG = LED(14)
ledB = LED(15)

while True:
    ledG.on()
    sleep(0.5)
    ledG.off()
    sleep(0.5)