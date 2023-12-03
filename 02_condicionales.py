# 1. Ejercicio: Dado un número, imprime si es positivo o negativo.
numero = float(input("Ingrese un número: "))
if numero > 0:
 print("El número es positivo")
elif numero < 0:
 print("El número es negativo")
# 2. Ejercicio: Dado un número, imprime si es par o impar.
if numero % 2 == 0:
 print("El número es par")
else:
 print("El número es impar")
# 3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
a = 5
b = 3
c = 4

if a >= b and a >= c:
 mayor = a
elif b >= a and b >= c:
 mayor = b
else:
 mayor = c

print(f"El número mayor es: {mayor}")