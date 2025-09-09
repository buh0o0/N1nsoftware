import math
from math import degrees
#voy hacer una funcion de una receta

#def preparar(Nombre,pasos):
 #   print(f"preparando {Nombre}")

  #  for pasos in pasos:
   #     print (f"{pasos}")
    #    print(f"{Nombre} listo!!")

##Ejemplo 1

#funcion que saluda

def saludar():
    print("HOLA")
    print("bienvenido")

saludar()

##Ejemplo 2
#funcion con argumentos
def saludarHumano(Nombre):
    print(f"HOLA ¿como estas? {Nombre.capitalize()}")
    print(f"HOLA ¿como estas? {Nombre.casefold()}")
    print(f"HOLA ¿como estas? {Nombre}")

saludarHumano(f"DANIEL ROJAS 123" )

#ejemplo 3
#funcion para calcular y devuelve resultado

def Sumar (a,b):
    Suma= a + b
    return Suma
#Usar y guardar el resultado
Total = Sumar(5,10)
print(f"la suma de los numeros es: {Total}")

##Funciones integradas
#ejemplo 1  ##sum
num1 = [1,2,3,4,5,6]
print(f"{sum(num1)}")

#ejemplo 2 ##type
a="texto"
b=1
c= True
print(f"el primer dato es de tipo {type(a)}")


##Funciones de modulos
        #ejemplo 1
print(math.sqrt(25)) # Usa la función sqrt del módulo math
        #ejemplo 2
print(degrees(1.57)) # Usa la función degrees directamente