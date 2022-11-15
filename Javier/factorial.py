#################################################################
# Calula el factorial de un número usando una función recursiva
#################################################################
# Devuelve el factorial de un número
def factorial(nn):
	if nn == 1:
		return 1
	return (nn *  factorial(nn - 1))
	
num = int(input("Introduce un número para calcular el factorial "))
if num < 0:
	print("El número tiene que ser positivo")
else:
	print("El factorial de "+ str(num) + " es " + str(factorial(num)))


