import time, random, os, threading

def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
         os.system ("cls")

#############################
# Clase filosofo
#############################
class filosofo():
    # propiedades de clase que tienen que ser visibles entre todas las instancias.
    estado_filosofo = [] 
    estado_palillo = []
    num_filosofos = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.id = filosofo.num_filosofos
        filosofo.estado_filosofo.append('se sienta en la mesa')
        filosofo.estado_palillo.append('libre')
        print(self.nombre + ' ' + filosofo.estado_filosofo[self.id] + ' y tiene su palillo de la derecha ' + filosofo.estado_palillo[self.id])
        filosofo.num_filosofos +=1 
    
    def piensa(self):
        #  cambio el estado y el filosofo se pone a pensar
        filosofo.estado_filosofo[self.id] = 'pensando'
        print(self.nombre + ' ' +filosofo.estado_filosofo[self.id])
        time.sleep(random.randint(1,5))
        # se ha cansado de pensar y tiene hambre, intenta coger los palillos
        self.intenta_comer()
     
    def intenta_comer(self):
        # Si puede coger los dos palilos come y si no espera
        if self.CogePalillos():
            self.come()
        else:
            self.espera()    
            
    def CogePalillos(self):
        # calcula el número de palillo que tiene a la izquierda
        vuelta = False
        if self.id == 0:
            PalilloIzquierda = 4
        else:
            PalilloIzquierda = self.id - 1
        
        # si izquierda y derecha están libres los coge 
        if filosofo.estado_palillo[self.id] == 'libre':
            filosofo.estado_palillo[self.id] = 'ocupado'
            if filosofo.estado_palillo[PalilloIzquierda] == 'libre':
                filosofo.estado_palillo[PalilloIzquierda] = 'ocupado'
                vuelta = True
            else:
                # el palillo de la izquierda no está libre, suelta el palillo de la derecha para que se pueda emplear
                filosofo.estado_palillo[self.id] = 'libre'
                # y espera su turno
        return vuelta
                   
    def espera(self):
        # espera unos segudos aleatorios y vuelve a intentarlo
        filosofo.estado_filosofo[self.id] = 'esperando'
        print(self.nombre + ' ' + filosofo.estado_filosofo[self.id])
        time.sleep(random.randint(1,5))
        self.intenta_comer()
        
    def come(self):
        filosofo.estado_filosofo[self.id] = 'comiendo'
        print(self.nombre + ' ' + filosofo.estado_filosofo[self.id])
        time.sleep(random.randint(1,5))  
        
        #he terminado de comer, suelto los palillos 
        filosofo.estado_palillo[self.id] = 'libre'     
        if self.id == 0:
            PalilloIzquierda = 4
        else:
            PalilloIzquierda = self.id - 1
        filosofo.estado_palillo[PalilloIzquierda] = 'libre'    
        # ya ha comido, se pone a pensar
        self.piensa()
        

##########################
def main():
    borrarPantalla()   
    numero_filosofos = 5
    lista=[]
    # se crea una instanacia de la clase filosofo por cada filosofo 
    for i in range(numero_filosofos):
        lista.append(filosofo("Filosofo " + str(i + 1))) 
   
    print('Ya se han sentado todos a la mesa') 
    print('')
    for filo in lista:
        # Declaro un hilo de ejecución para que todos los objetos (filosofos) puedan interactuar entre si.
        empieza_a_comer = threading.Thread(target=filo.piensa)
        empieza_a_comer.start()

        
##########################
if __name__=="__main__":
    main()