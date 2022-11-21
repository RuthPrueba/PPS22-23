numero = int(input("Dígame un numero "))
f = 1
h = 0
suma = numero

def factorial(n,f):
    for i in range(1,n):
        f = f*i
        h = n*i
        print(n,"*", i, "=", h)
    return f

if numero < 0:
  print("noooo numeros negaativos")
elif numero == 0:
  print("factorial = 1")
else:
  print("El factorial iterativo de", numero, "es", factorial(numero,suma))

