##complete los ejercicios
##1)
'''
def cuadrado(numero):
    return numero*numero

print(cuadrado(4))
print(cuadrado(5))
##2)
def sumar(a,b):
    resultado=a+b
    return resultado

print(f"la suma es",sumar(4,5))
### funciones 
# usando la (f)(f-es string)
nombre="luz"
edad="80"
print(f"hola {nombre}, tienes {edad}")
'''
#### LA CONDICIONAL IF
edad2=21
if edad2 <= 18:
    print("eres menor de edad no puedes tomar")
else:
    print("puedes tomar alcohol")

#############  EJERCICIOS ################

##PEDIR AL ESTUDIANTE UNA NOTA ENTRE 0 Y 100 EN UN INPUT
nota=int(input("elija un numero entre 0 y 100"))

##CREAR UN PROGRAMA QUE PIDA LA EDAD AL USUARIO Y MUESTRE SI ES NIÑO,ADOLECENTE, ADULTO O ADULTO MAYOR
edad = int(input("ingrese su edad, porfavor"))
if edad <= 13:
    print("usted es un niño")
elif edad >13 or edad <=18:
    print("usted es un adolecentes")

##PIDE EL COLOR DEL SEMAFORO(ROJO/AMARILLO/VERDE)

decision=str(input("digame el color del semaforo"))

if decision == "rojo" or "Rojo" or "red" :
    print("Detenerse")
elif decision == "Verde":
    print("avance")
elif decision == "amarillo":
    print("Detengase")
else:
    print("no es un color valido")