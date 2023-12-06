# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
def segundo_mas_grande(lista):
 if len(lista) < 2:
  return "La lista debe estar formada mínimo por dos números"
 ordenar_lista = sorted(set(lista), reverse=True)
 segundo_mas_grande = ordenar_lista[1]
 return segundo_mas_grande
lista_numeros = [3,4,2,5,1,6,2]
resultado = segundo_mas_grande(lista_numeros)
print(resultado)

# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def miembro_comun(listaA, listaB):
 for elemento in listaA:
  if elemento in listaB:
   return True
 return False
listaA = [1,2,3,4,5]
listaB = [1,6,7,8,9]
resultado_comun = miembro_comun(listaA, listaB)
print(resultado_comun)

# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def orden_inverso(lista):
 lista_inversa = lista.copy()
 lista_inversa.reverse()
 return lista_inversa
lista_inversa = [1,2,3,4,5]
resultado_inversa = orden_inverso(lista_inversa)
print(resultado_inversa)

# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def contar_digitos(cadena):
 digitos = 0
 numeros = 0
 for caracter in cadena:
  if caracter.isdigit():
   digitos += 1
  elif caracter.isalpha():
   numeros += 1
  return digitos, numeros
cadena_ejemplo = "Hola7"
resultado_contar_digitos = contar_digitos(cadena_ejemplo)
print(resultado_contar_digitos)

# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_numeros(lista):
 suma = 0
 resultado = []
 for caracter in lista:
  suma += caracter
  resultado.append(suma)
 return resultado
lista_suma_numeros = [1,2,3,4]
resultado_suma = suma_numeros(lista_suma_numeros)
print(resultado_suma)

# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
def elemento_mas_comun(lista):
 frecuencia = {}
 for elemento in lista:
  if elemento in frecuencia:
   frecuencia[elemento] += 1
  else:
   frecuencia[elemento] = 1
 elemento_comun = max(frecuencia, key=frecuencia.get)
 return elemento_comun
lista_repetida = [1,1,1,1,1,2,2,3,5,5,5,6]
resultado_repetidos = elemento_mas_comun(lista_repetida)
print(resultado_repetidos)

# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
def tabla_multiplicar(numero):
 resultado_multiplicar = {}
 for i in range(1, 11):
  resultado_multiplicar[i] = numero * i
 return resultado_multiplicar
numero_multiplicar = 7
resultado_multiplicar = tabla_multiplicar(numero_multiplicar)
print(resultado_multiplicar)

# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
def caracter_repetido(cadena):
 repeticiones = {}
 for caracter in cadena:
  repeticiones[caracter] = repeticiones.get(caracter, 0) + 1
 return repeticiones
cadena_repeticiones = "HolaMundo"
resultado_repeticiones = caracter_repetido(cadena_repeticiones)
print(resultado_repeticiones)

# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def elemento_no_repetido(listaA, listaB):
 unicos_listaA = set(listaA) - set(listaB)
 unicos_listaB = set(listaB) - set(listaA)
 no_repetidos = list(unicos_listaA.union(unicos_listaB))
 return no_repetidos
resultado_listaA = [1,2,3,4,5,6]
resultado_listaB = [3,4,5,6,7,8]
resultado_no_repetidos = elemento_no_repetido(resultado_listaA, resultado_listaB)
print(resultado_no_repetidos)

# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
def no_duplicados(lista):
 lista_no_duplicados = list(set(lista))
 return lista_no_duplicados
lista_no_duplicados = [1,1,1,2,3,3]
resultado_no_duplicados = no_duplicados(lista_no_duplicados)
print(resultado_no_duplicados)

# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
def suma_cuadrados(numero):
 if not isinstance(numero, int) or numero < 0:
  return "Actualice el valor a un número positivo"
 suma = sum(x**2 for x in range(2, numero + 1, 2))
 return suma
numero_cuadrado = 6
resultado_cuadrado = suma_cuadrados(numero_cuadrado)
print(resultado_cuadrado)

# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
def promedio(lista):
 suma = sum(lista)
 elementos_lista = len(lista)
 promedio_lista = suma / elementos_lista
 return promedio_lista
lista_promedio = [1,2,3,4,5]
resultado_promedio = promedio(lista_promedio)
print(resultado_promedio)

# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_larga(lista):
 cadena_larga = max(lista, key=len)
 return cadena_larga
lista_cadenas = ['Hola', 'Que', 'Tal']
resultado_cadena_larga = cadena_mas_larga(lista_cadenas)
print(resultado_cadena_larga)

# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
def n_primos(num):
 if num < 2:
  return False
 for i in range(2, int(num**0.5) + 1):
  if num % i == 0:
   return False
 return True

def numero_primo(n):
 primos = []
 numero = 2
 while len(primos) < n:
  if n_primos(numero):
   primos.append(numero)
  numero += 1
 return primos
ejemplo_primo = 5
resultado_primo = numero_primo(ejemplo_primo)
print(resultado_primo)

# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def orden_inverso(cadena):
 cadena_invertida = cadena[::-1]
 return cadena_invertida
cadena_inversa = ['Primero', 'Segundo', 'Tercero']
resultado_cadena_inversa = orden_inverso(cadena_inversa)
print(resultado_cadena_inversa)

# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
# key=lambda tupla: tupla[-1] -> Ordena la lista basándose en el último elemento.
def ordenar_tupla(tupla):
 tupla_ordenada = sorted(tupla, key=lambda tupla: tupla[-1])
 return tupla_ordenada
ejemplo_tupla = [(1,2,3), (5,2,1)]
resultado_tupla = ordenar_tupla(ejemplo_tupla)
print(resultado_tupla)

# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
def cantidad_vocales(cadena):
 cadena = cadena.lower()
 vocales = 'aeiou'
 total_vocales = sum(1 for letra in cadena if letra in vocales)
 return total_vocales
ejemplo_vocales = 'Bienvenidos'
resultado_vocales = cantidad_vocales(ejemplo_vocales)
print(resultado_vocales)

# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
def numero_primo(numero):
 if numero <= 1:
  return False
 for i in range(2, int(numero**0.5) + 1):
  if numero % i == 0:
   return False
 return True
ejemplo_primo = 19
resultado_numero_primo = numero_primo(ejemplo_primo)
print(resultado_numero_primo)