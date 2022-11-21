import threading
import time
import random

estadoFilosofo = None
palillo = []
nfilosofos = int(input("Dígame el número de filosofos que quieran comer:"))
maxmuerte = 10   

pensando = "F"
comiendo = "C"


def cogerpalillo(numero):
    der = palillo[numero]
    izq = palillo[(numero - 1) % nfilosofos]
    der.acquire()
    if izq.acquire(blocking=False):
        return True
    else:
        der.release()
        return False

def soltarpalillo(numero):
    palillo[numero].release()
    palillo[(numero - 1) % nfilosofos].release()

def iniciarSimulacion(numero):
    intentos_fallidos = 0
    tiempo_comiendo = 0
    while tiempo_comiendo < 5:
        if cogerpalillo(numero):
            intentos_fallidos = 0
            print(f"El filosofo {numero + 1} ahora está comiendo")
            soltarpalillo(numero)
            estadoFilosofo[numero] = pensando
            tiempo_pensando = random.uniform(0, 5)
            print(f"El filosofo {numero + 1} ahora está pensando")
            time.sleep(tiempo_pensando)
        else:
            tiempo_reintentar = random.uniform(0, 3)
            time.sleep(tiempo_reintentar)
        
if __name__ == '__main__':
    estadoFilosofo = nfilosofos * [pensando]
    for _ in range(nfilosofos):
        palillo.append(threading.RLock())
    hilos = []
    for i in range(nfilosofos):
        nuevo_hilo = threading.Thread(target=iniciarSimulacion, args=(i,))
        hilos.append(nuevo_hilo)
    for hilo in hilos:
        hilo.start()
