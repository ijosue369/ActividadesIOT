'''
Equipo:
 - Aguirre Villanueva Juan Carlos
 - López Terán Irving Josué
 - Siles Asaff Juan Pablo
'''
#%%
from gpiozero import LED
from time import sleep
import psutil 

ledR = LED(16)
ledG = LED(20)
ledY = LED(21)

while True:
    cpuPorcentaje = int(psutil.cpu_percent(interval=1))
    print(cpuPorcentaje)
    if cpuPorcentaje <= 10:
        ledR.off()
        ledG.on()
        ledY.off()
    elif cpuPorcentaje > 10 and cpuPorcentaje <= 20:
        ledR.off()
        ledG.off()
        ledY.on()
    elif cpuPorcentaje > 20:
        ledG.off()
        ledG.off()
        ledR.on()
        sleep(1)
        ledR.off()
        sleep(1)
    else:
        ledR.off()
        ledG.off()
        ledY.off()
# %%
