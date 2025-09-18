## 17/09/2025
#Que es una lista
##una lista es una estructura de datos que permite guardar varios datos
##ejemplos
##crear una lista
frutas=["manzana","peras","mangos"]
print(frutas)
## ejercicio 2, cada elemento tiene un indice
print(frutas[0])
print(frutas[1])
print(frutas[2])

## modificar una lista por su indice
# por indice. puedes cambar un elemento accediendo a su posicion
#ejemplo
frutas2 = ["manzana","pera","naranja"]
frutas2[1]="banano"
print(f"Lista actualizada {frutas2}")

########## METODOS

## Append
colores=["rojo","amarillo","verde","azul"]
colores.append("negro")##agrega un elemento al final de la lista

## Insert
colores.insert(1,"blanco")## inserta un elemento en el indice especificado
print(f"la lista de colores es: {colores}")

## Pop
animales=["vaca","perro","gato","mico","juan"]
animales.remove("vaca")
animal = animales.pop(),
print(f"la lista quedo : {animales} y el metodo pop extrajo el dato de: {animal}")

## Sort
numeros=[5,4,7,3,9,19,45,7,6]
numeros.append(9999)
numeros.sort()
print(numeros)
## Ejercicio con for
nombres=["ana","maria","luisa","fernanda"]
print("Lista de nombre")
for nombre in nombres:
    print(nombre)



