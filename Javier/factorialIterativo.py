#######################################
# calcula un factorial con un bucle
######################################

numero = int(input("Introduce un número entero para calcular el factorial "))

if numero < 0:
	print("El número tiene que ser positivo")
else:
	
	valor = numero
	num = numero
	while num >= 2:
		num = num - 1
		valor = valor * num 
		
	print("El factorial de "+ str(numero) + " es: " + str(valor))




