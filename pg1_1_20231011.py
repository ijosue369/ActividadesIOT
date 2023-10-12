''' 
Equipo:
 - Aguirre Villanueva Juan Carlos
 - López Terán Irving Josué
 - Siles Asaff Juan Pablo
'''
from gpiozero import LED, Button
from time import sleep

listaColores = [
    {
        "Color" : "Rojo",
        "Salida" : 16
    },
    {
        "Color" : "Verde",
        "Salida" : 20
    },
    {
        "Color" : "Azul",
        "Salida" : 21
    }
]
    
while True:
    color = input("Selecciona el color: ")
    parpadeo = input("¿Parpadeo? (0 = no, 1 = sí): ")
    DiccionarioColor = [x for x in listaColores if x[color] == color][0]
    if parpadeo == "0":
        LED(DiccionarioColor.values(1)).on()
    elif parpadeo == "1":
        LED(DiccionarioColor.values(1)).on()
        sleep(0.5)
        LED(DiccionarioColor.values(1)).off()
        sleep(0.5)
# %%
