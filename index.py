## La suma de dos numeros y dos operaciones mas
'''
a=5;
b=5;
print("la suma es ", a+b);
print("la resta es ", a-b);
print("la division es ", a/b);'''
## Algoritmo suma con entrada de usuario
'''
c=int(input("ingresa el primer numero "))
d=int(input("ingresa el segundo numero "))

suma = c+d;
multiplicacion= c*d
division = c/d

print("la suma es : ", suma);
print("la multiplicacion es : ", multiplicacion)
print("la division es : ", division) '''

##imprima el primer elemento de una lista 
lista = ["carro","moto","bici"]
print(lista[0])

## cree 5 algoritmos de nivel intermedio

            ##1 algoritmo para crear sacar un promedio
estudiantes = {
    "Ana": [4.5, 3.8, 4.2],
    "Luis": [2.9, 3.0, 2.5],
    "Sofía": [3.5, 3.7, 4.0],
    "Carlos": [2.0, 2.5, 3.0]
}
## Función para calcular el promedio
def calcular_promedio(notas):
    return sum(notas) / len(notas)
## Evaluar cada estudiante
for nombre, notas in estudiantes.items():
    promedio = calcular_promedio(notas)
    estado = "Aprobado" if promedio >= 3.0 else "Reprobado"
    print(f"{nombre}: Promedio = {promedio:.2f} → {estado}")

            ##### 2 Algoritmo de conversión de unidades
def convertir_unidad(valor, tipo_conversion):
    if tipo_conversion == "C a F":
        return valor * 9/5 + 32
    elif tipo_conversion == "F a C":
        return (valor - 32) * 5/9
    elif tipo_conversion == "km a mi":
        return valor * 0.621371
    elif tipo_conversion == "kg a lb":
        return valor * 2.20462
    else:
        return "Conversión no válida"

print(convertir_unidad(100, "C a F"))  # 212.0

        ### 3 Algoritmo para detectar números primos en una lista

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_en_lista(lista):
    return [num for num in lista if es_primo(num)]

numeros = [10, 13, 17, 20, 23, 29, 30]
print(primos_en_lista(numeros))  # [13, 17, 23, 29]

## 4 Algoritmo para calcular la edad a partir de la fecha de nacimiento
from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.today()
    nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

# Ejemplo 
print(calcular_edad("2000-09-01"))  # Devuelve la edad actual


##5 Algoritmo: Contador de letras en una frase

# Esta función cuenta cuántas veces aparece cada letra en una frase
def contar_letras(frase):
    frase = frase.lower()  # Convertimos todo a minúsculas para evitar duplicados por mayúsculas
    contador = {}  # Creamos un diccionario vacío para guardar las letras y sus cantidades

    for letra in frase:
        if letra.isalpha():
            if letra in contador:
                contador[letra] += 1  # Si ya existe la letra, sumamos 1
            else:
                contador[letra] = 1  # Si no existe, la agregamos con valor 1

    # Mostramos el resultado
    for letra, cantidad in contador.items():
        print(f"La letra '{letra}' aparece {cantidad} veces.")

# Ejemplo de uso
frase_usuario = input("Escribe una frase: ")
contar_letras(frase_usuario)

