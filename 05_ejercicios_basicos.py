# 1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar”según corresponda
def es_par(numero): 
  if numero % 2 == 0:
   return "El número es par"
  else: 
   return "El número es impar"
prueba_par = 2
resultado_par = es_par(2)
print(resultado_par)

# 2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
def factorial(numero):
 if numero == 0 or numero == 1:
  return 1
 else:
  return numero * factorial(numero - 1)
prueba_factorial = 7
resultado_factorial = factorial(prueba_factorial)
print(resultado_factorial)

# 3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
# len = calcula la longitud del elemento.
# str = convierte cualquier valor a string.
def string(numero):
 longitud = len(str(numero))
 print(f"La longitud de: {numero} es: {longitud}")
ejemplo_longitud = 637386
resultado_longitud = string(ejemplo_longitud)

# 4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.
# max = saca el máximo valor.
def num_max(numero):
 result = max(numero)
 return result
numeros = [3,4,5,6,7,8,2,85,105,2]
resultado_num_max = num_max(numeros)
print(resultado_num_max)

# 5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
# int = convierte los valores a números enteros.
def suma_digitos(numero):
 suma = 0
 for digito in str(numero):
  suma += int(digito)
 return suma
ejemplo_numero_suma = 123123
resultado_numero_suma = suma_digitos(ejemplo_numero_suma)
print(resultado_numero_suma)

# 6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM
def mcm(numA, numB):
 def calculo_mcm(a, b):
  while b:
   a, b = b, a % b
  return a

 return abs(numA * numB) // calculo_mcm(numA, numB)
numA = 2
numB = 18
resultado_mcm = mcm(numA, numB)
print(resultado_mcm)

# 7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo
def area_triang(base, altura):
 area = base * altura / 2
 return area
base = 5
altura = 4
area_total = area_triang(base, altura)
print(area_total)

# 8. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
def valor_num(numero):
  if numero > 0:
    return "El número es positivo"
  elif numero < 0:
    return "El número es negativo"
  else:
    return "El número es 0"
ejemplo_valor = 4
resultado_valor = valor_num(ejemplo_valor)
print(resultado_valor)

# 9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
def contar_letras(palabra):
  cantidad_total = len(palabra)
  return cantidad_total
ejemplo_palabra = "Holaquetal"
resultado_ejemplo_palabra = contar_letras(ejemplo_palabra)
print(resultado_ejemplo_palabra)

# 10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
def absoluto(lista):
  lista_absoluta = [abs(numero) for numero in lista]
  return lista_absoluta
ejemplo_lista = [4,-29,30,40,-115]
resultado_lista_absoluta = absoluto(ejemplo_lista)
print(resultado_lista_absoluta)

# 11. Crea una función que, dado un número, verifique si un número es primo.
def primo(numero):
  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
      return False
  return True
ejemplo_primo = 4
resultado_primo = primo(ejemplo_primo)
print(resultado_primo)

# 12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números
def calculo_mcd(numA, numB):
  while numB:
    numA, numB = numB, numA % numB
  return abs(numA)
numA = 12
numB = 2
resultado_mcd = calculo_mcd(numA, numB)
print(resultado_mcd)
