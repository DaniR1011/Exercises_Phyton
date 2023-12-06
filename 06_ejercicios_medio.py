# Ejercicios del 1 al 17 🚀

# 1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros números de la serie de Fibonacci.
def fibonacci(n):
 a, b = 0, 1
 for _ in range(n):
  print(a, end=" ")
  a, b = b, a + b
ejemplo_fibonacci = 20
fibonacci(ejemplo_fibonacci)

# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
def divisores(numero):
 divisores_totales = []
 for i in range(1, numero + 1):
  if numero % i == 0:
   divisores_totales.append(i)
  return divisores_totales
ejemplo_divisores = 18
resultado_divisores = divisores(ejemplo_divisores)
print(f"Los divisores de {ejemplo_divisores} son: {resultado_divisores}")

# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
# list = es una lista ordenada en Python.
# set = elimina los duplicados de la lista.
def elementos_unicos(lista):
 total_elementos = list(set(lista))
 return total_elementos
lista_ejemplo = [1,2,3,3,3,3,5]
resultado_unicos = elementos_unicos(lista_ejemplo)
print(f"La lista con elementos únicos: {resultado_unicos}")

# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
# int = convierte valores a números enteros.
def sum_digitos(numero):
 total_digitos = str(numero)
 suma = 0
 for digito in total_digitos:
  suma += int(digito)
 return suma
ejemplo_digito = 321
resultado_digito = sum_digitos(ejemplo_digito)
print(resultado_digito)

# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
# .lower() = transforma todo a minúsculas.
def contar_vocales(list):
 list = list.lower()
 vocales = 'aeiou'
 contador = 0
 for vocal in list:
  if vocal in vocales:
   contador += 1
  return contador

# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def obtener_n(lista, n):
 return lista[:n]
lista_num = [1,2,3,5,6,7,8,9]
n_totales = 5
resultado_obtener_n = obtener_n(lista_num, n_totales)
print(resultado_obtener_n)

# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
# isupper = verifica que todos los caracteres están en mayus.
def mayus_minus(cadena):
 mayus = 0
 minus = 0
 for caracter in cadena:
  if caracter.isupper():
   mayus += 1
  elif caracter.islower():
   minus += 1
  resultados = {
   'mayus': mayus,
   'minus': minus
  }
  return resultados
ejemplo_cadena = 'Buenos Días'
resultado_cadena = mayus_minus(ejemplo_cadena)
print(resultado_cadena)

# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
def numero_perfecto(numero):
 if numero <= 0:
  return False
 divisores_totales = 0
 for i in range(1, numero // 2 + 1):
  if numero % i == 0:
   divisores_totales += i
 return divisores_totales == numero
ejemplo_perfecto = 6
resultado_perfecto = numero_perfecto(ejemplo_perfecto)
print(resultado_perfecto)

# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
def binario(numero):
 binario = bin(numero)
 binario_ejemplo = binario[2:]
 return binario_ejemplo
ejemplo_binario = 2
resultado_binario = binario(ejemplo_binario)
print(resultado_binario)

# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
# set = representa una lista con datos no ordenados y sin que estén repetidos.
def interseccion(listaA, listaB):
 interseccion = list(set(listaA) & set(listaB))
 return interseccion
listaA = [1,2,3,4]
listaB = [0,1,5,6]
resultado_interseccion = interseccion(listaA, listaB)
print(resultado_interseccion)

# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def palindrono(cadena):
 cadena = ''.join(e.lower() for e in cadena if e.isalnum())
 return cadena[::-1]
cadena_ejemplo = "Dábale arroz a la zorra el abad"
resultado_palidrono = palindrono(cadena_ejemplo)
print(resultado_palidrono)

# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
for numero in range(1, 51):
 if numero % 3 == 0:
  print('Fizz')
 elif numero & 5 == 0:
  print('Buzz')
 elif numero % 3 == 0 and numero % 5 == 0:
  print('FizzBuzz')
 else:
  print(numero)

# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
# sort = sirve para ordenar una lista.
def ascendente(lista):
 lista.sort()
ejemplo_ascendente = [5,7,2,8,0,32,1]
ascendente(ejemplo_ascendente)
print(f"La lista ordenada es: {ejemplo_ascendente}")

# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
def palabra_mas_larga_n(lista, n):
 palabras = [palabra for palabra in lista if len(palabra) > n]
 return palabras
ejemplo_lista = ["python", "javascript", "react", "HTML", "CSS", "bucle", "variable", "funciones"]
n = 5
resultado_palabra_larga = palabra_mas_larga_n(ejemplo_lista, n)
print(resultado_palabra_larga)

# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
def fibonacci(numero):
 if numero <= 0:
  return "Número mayor a 0"
 elif numero == 1:
  return [0]
 else:
  serie_fibonacci = [0, 1]
  while len(serie_fibonacci) < n:
   serie_fibonacci.append(serie_fibonacci[-1] + serie_fibonacci[-2])
  return serie_fibonacci
ejemplo_fibonacci_cadena = 5
resultado_fibonacci = fibonacci(ejemplo_fibonacci_cadena)
print(resultado_fibonacci)

# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
def numero_mas_grande(lista):
 if not lista:
  return "Lista vacía"
 maximo = max(lista)
 return maximo
lista_numeros = [14,3,45,68,4,3]
resultado_numero = numero_mas_grande(lista_numeros)
print(resultado_numero)

# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
def suma_al_cubo(numero):
 numero_string = str(numero)
 suma = sum(int(digito) ** 3 for digito in numero_string)
 return suma
ejemplo_suma_cubo = 22
resultado_cubo = suma_al_cubo(ejemplo_suma_cubo)
print(resultado_cubo)