def fibonacci(n):
	if n == 1 or n == 0:
		return n + 0 or n + 1

	else:
		return fibonacci(n-2) + fibonacci(n-1)

numero = int(input("Ingrese un numero entero positivo: "))

if numero < 0:
	print("Numero no valido")
	
	i = 0

print("Sucesión de fibonacci")

for i in range(0, numero):
	print(fibonacci(i))

	
	

