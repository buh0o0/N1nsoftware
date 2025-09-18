##Estructura repetitiva ######15/09/2025##

### FOR ###
nombres =["ana","camilo","juan","daniel"]
#Ejercicio1
for nombre in nombres:
    print(nombre.upper()) ##pone en mayusculas todas las letras 
#Ejercicio 2
for nombre in nombres:
    print(nombre.startswith("a")) ##verifica si la primera letra de cada cadena coincide con lo especificado
#Ejercicio 3
animales = ["perro","gato","pajaro","tortuga"]
for animal in animales:
    print(animal.capitalize()) ##genera la primera letra en mayuscula
#Ejercicio 4
for animal in animales:
    print("$".join(animal)) ## agrego el texto que quiera entre cada caracter o cadena de texto

## WHILE ##
contrasena="f"
conteo= 0
while contrasena != "python" and conteo <= 2:
    conteo = conteo + 1
    contrasena = input("digite la contraseña")
    print("tienes 3 oportunidades , vas :",conteo)
if contrasena == "python":
    print("acceso permitido")
else:
    print("accesos denegado")
####  EJERCICIOS ####
#imprimir numeros del 1 al 10 con for
numeros= [1,2,3,4,5,6,7,8,9,10]
for  numero in numeros:
   print(numero)
##contar regresivamente con while que me muestre los numeros del 5 al 1
contar=5
while contar >= 1:
    print(contar)
    contar -= 1

## con for haga una tabla de multiplicar que muestre la del 3

for numero in numeros:
    resultado=numero*3
    print(f"{numero} * 3  =  {resultado}")
