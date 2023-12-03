# 1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
 print(numero)
# 2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
numero = 1
while numero <= 20:
 if numero % 2 == 0:
  print(numero)
 numero += 1
# 3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
suma = 0
for numero in range(1, 101):
 suma += numero
print("La suma de los numeros del 1 al 100 es:", suma)