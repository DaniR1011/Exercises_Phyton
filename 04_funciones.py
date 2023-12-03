# 1. Ejercicio: Define una función que tome dos números y retorne su suma.
def suma(a,b):
 total = a + b
 return (total)
resultado = suma(5,9)
print("La suma es:", resultado)
# 2. Ejercicio: Define una función que tome un número y retorne su factorial.
def factorial(numero):
 if numero == 0 or numero == 1:
  return 1
 else:
  return numero * factorial(numero - 1)

ejemplo = 5
resultado = factorial(ejemplo)
print(f"El factorial de {ejemplo} es: {resultado}")
# 3. Ejercicio: Define una función que tome un número y determine si es primo.
def primo(numero):
 if numero < 2:
  return False
 for i in range(2, int(numero**0.5) + 1):
  if numero % 1 == 0:
   return False
  return True

ejemplo_primo = 13
if primo(ejemplo_primo):
 print(f"{ejemplo_primo} es un número primo.")
else:
 print(f"{ejemplo_primo} no es un número primo")
# 4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
def suma_total(numeros):
 total = sum(numeros)
 return total

numeros_a_sumar = [4,3,6,78]
resultado_total = suma_total(numeros_a_sumar)
print(f"El resultado total es {resultado_total}")
# 5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
# ::-1 invertimos la cadena de texto
def texto(cadena):
 invertida = cadena[::-1]
 return invertida

texto_ejemplo = "Hola esto es un ejemplo"
texto_resultado = texto(texto_ejemplo)
print(f"Texto ejemplo: {texto_ejemplo}")
print(f"Texto invertido: {texto_resultado}")