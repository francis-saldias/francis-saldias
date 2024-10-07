# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 22:11:10 2023

@author: franc
"""
nombre_Jugador1 = input("Jugador 1, ingrese su nombre: ")
while len(nombre_Jugador1) < 3 or len(nombre_Jugador1) > 20:
    print("El nombre debe ser de mínimo 3 carácteres y máximo 20")
    nombre_Jugador1 = input("Jugador 1, reingrese su nombre: ")
nombre_Jugador2 = input("Jugador 2, ingrese su nombre: ")
while len(nombre_Jugador2) < 3 or len(nombre_Jugador2) > 20:
    print("El nombre debe ser de mínimo 3 carácteres y máximo 20")
    nombre_Jugador2 = input("Jugador 2, reingrese su nombre: ")
print()
print("¡Bienvenidos al juego", nombre_Jugador1 + " y " + nombre_Jugador2 + "!")
print()
import verbosDefinicion
from datetime import datetime
from time import sleep
start_Jugador1 = datetime.now()
aciertos_Jugador1= 0
for i in range(3):
    verbo_español = verbosDefinicion.getDefinicion()
    verbo_inglés = verbosDefinicion.getVerbo(verbo_español)
    print(nombre_Jugador1,"escribe en inglés el verbo a continuación: ",verbo_español)
    respuesta = input("Respuesta: ")
    if respuesta == verbo_inglés:
        aciertos_Jugador1 += 1
        print("¡Muy bien", nombre_Jugador1 + ", has acertado!")
    else:
        print("Incorrecto :( La respuesta correcta era:",verbo_inglés)
        print()
if aciertos_Jugador1 == 3:
        print("¡Excelente", nombre_Jugador1 + ".", "has acertado todas!")
elif aciertos_Jugador1 >= 1:
        print("Lo has hecho bien", nombre_Jugador1 + "." , "Has acertado", aciertos_Jugador1, "de 3" )
else:
        print("Al parecer deberás seguir estudiando", nombre_Jugador1 + ".", "Has tenido 0 aciertos de 3 :c")
sleep(2)
end_Jugador1 = datetime.now()
demora_Jugador1= (end_Jugador1 - start_Jugador1).total_seconds()
print()
print("Ahora es el turno de", nombre_Jugador2)
print()
start_Jugador2 = datetime.now()
aciertos_Jugador2 = 0
for i in range(3):
        verbo_español = verbosDefinicion.getDefinicion()
        verbo_inglés = verbosDefinicion.getVerbo(verbo_español)
        print(nombre_Jugador2 + ", escribe en inglés el verbo a continuación: ",verbo_español)
        respuesta = input("Respuesta: ")
        if respuesta == verbo_inglés:
            aciertos_Jugador2 += 1
            print("¡Muy bien", nombre_Jugador2 + ", has acertado!")
        else:
            print("Incorrecto :( La respuesta correcta era:",verbo_inglés)
if aciertos_Jugador2 == 3:
        print("¡Excelente", nombre_Jugador2 + ".", "has acertado todas!")
elif aciertos_Jugador2 >= 1:
        print("Lo has hecho bien", nombre_Jugador2 + "." , "Has acertado", aciertos_Jugador2, "de 3" )
else:
        print("Al parecer deberás seguir estudiando", nombre_Jugador2 + ".", "Has tenido 0 aciertos de 3 :c")   
sleep(2)
end_Jugador2 = datetime.now()
demora_Jugador2= (end_Jugador2 - start_Jugador2).total_seconds()
print()
if aciertos_Jugador1 > aciertos_Jugador2:
    print("Felicidades", nombre_Jugador1 + ", has ganado el juego. Acertaste", aciertos_Jugador1, "y", nombre_Jugador2, aciertos_Jugador2)
elif aciertos_Jugador2 > aciertos_Jugador1: 
    print("Felicidades", nombre_Jugador2 + ", has ganado el juego. Acertaste", aciertos_Jugador2, "y", nombre_Jugador1, aciertos_Jugador1)
elif aciertos_Jugador1 == 0 and aciertos_Jugador2 == 0:
    print("Resultado final: Ambos deberán seguir estuadiando, han tenido 0 aciertos")
elif aciertos_Jugador1 == aciertos_Jugador2:
            if demora_Jugador1 > demora_Jugador2:
                print("Felicidades", nombre_Jugador2 + ", has ganado el juego, tardaste", demora_Jugador2, "y", nombre_Jugador1, "tardó", demora_Jugador1)
            elif demora_Jugador2 > demora_Jugador1:
                print("Felicidades", nombre_Jugador1 + ", has ganado el juego, tardaste", demora_Jugador1, "y", nombre_Jugador2, "tardó", demora_Jugador2)
else: 
            print(nombre_Jugador1, "y", nombre_Jugador2 + ", han empatado.")