from gpiozero import LED, Button
import time
import random
import threading
import multiprocessing

print('Este se llama el juevo avanzado')

class Jugador(object):
    def __init__(self, button_io:int, led_io:int, jugador:int, tiempo_restante=30):
        self.button_io = Button(button_io)
        self.led_io = LED(led_io)
        self.tiempo_restante = tiempo_restante
        self.jugador = jugador
        self.conteo = 0

    def click(self):
        self.led_io.on()
        duracion = random.uniform(2, 8)
        start = time.time()
        while duracion > 0 and self.tiempo_restante > 0:
            if self.button_io.is_pressed:
                if not self.button_io.is_pressed:
                    self.conteo += 1
            duracion = time.time() - start
            self.tiempo_restante -= duracion
        self.led_io.off()
        return

    def pause(self):
        duracion = random.uniform(4, 8)
        start = time.time()
        while duracion > 0 and self.tiempo_restante > 0:
            self.led_io.on()
            if self.button_io.is_pressed:
                self.conteo -= 5
            duracion = time.time() - start
            self.tiempo_restante -= duracion
        return
    
    def start(self):
        while self.tiempo_restante > 0:
            self.click()
            self.pause()
        print(f'El jugador {self.jugador} dió {self.conteo}')

    def run(self):
        print(self.jugador)

jugador1 = Jugador(button_io=8, led_io=10, jugador=1)
jugador2 = Jugador(button_io=38, led_io=40, jugador=2)

jugador1 = threading.Thread(target=Jugador(button_io=8, led_io=10, jugador=1)).run()
jugador2 = threading.Thread(target=Jugador(button_io=38, led_io=40, jugador=2)).run()

jugador1.start()
jugador2.start()