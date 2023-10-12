''' 
Equipo:
 - Aguirre Villanueva Juan Carlos
 - López Terán Irving Josué
 - Siles Asaff Juan Pablo
'''
from gpiozero import LED, Button
from time import sleep
 
ledR = LED(16)
ledG = LED(20)
ledB = LED(21)

while True:
    ledG.on()
    sleep(0.5)
    ledG.off()
    sleep(0.5)