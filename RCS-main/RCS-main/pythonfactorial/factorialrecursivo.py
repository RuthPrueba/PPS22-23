numero = int(input("Dígame un numero "))
f = 1
h = 0

def factorial(num):
    if (num == 1):

        return num
    else:
        return num * factorial(num-1)

if numero < 0:
  print("noooo numeros negaativos")
elif numero == 0:
  print("factorial = 1")
else:
  print("El factorial iterativo de", numero, "es", factorial(numero))