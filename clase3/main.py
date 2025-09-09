
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
##ejemplo 1
import datetime
import calendar

def info_tiempo():
    ahora = datetime.datetime.now()
    fin_de_anio = datetime.datetime(ahora.year, 12, 31)
    dias_restantes = (fin_de_anio - ahora).days
    dia_semana = calendar.day_name[ahora.weekday()]
    
    return f"Hoy es {dia_semana}, {ahora.strftime('%d/%m/%Y %H:%M:%S')}. Faltan {dias_restantes} días para fin de año."


print(info_tiempo())

## ejemplo 2

import random
import math

def numero_magico():
    numero = random.randint(1, 100)
    raiz = math.sqrt(numero)
    
    return f"El número aleatorio es {numero} y su raíz cuadrada es {raiz:.2f}"

# Ejemplo de uso
print(numero_magico())

