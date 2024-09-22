# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:07:51 2024

@author: francis
"""
#importamos la librería
import turtle

# Configuración del fondo
window = turtle.Screen()
window.bgcolor("light blue")

# Creación del lapiz y su velocidad
pen = turtle.Turtle()
pen.speed(7)

# Función para dibujar un pétalo
def dibujar_petalo():
    pen.color("yellow") # Elegir el color para todos los pétalos
    pen.begin_fill()
    for _ in range(2):
        pen.circle(50, 60)  # Fijar los parámetros para la curva del pétalo
        pen.left(120)
    pen.end_fill()

# Función para dibujar el centro de la flor
def dibujar_centro():
    pen.color("orange") # Elegir el color
    pen.begin_fill()
    pen.circle(10)  # Centro de la flor
    pen.end_fill()

# Función para dibujar el tallo, será el mismo tipo para cada flor
def dibujar_tallo():
    pen.color("green")
    pen.setheading(-90)  # Fijamos en -90 para que sea vertical y hacia abajo
    pen.pendown()
    pen.forward(100)  # Longitud del tallo
    pen.penup()

# Función para dibujar la flor completa, con tallo, centro y pétalos
# Recordar los ejes x e y para determinar la posición de los elementos:
# Eje X: valores positivos mueven hacia la derecha, y negativos hacia la izquierda.
# Eje Y: valores positivos mueven hacia arriba, y negativos hacia abajo.
def dibujar_flor():
    dibujar_tallo()
    pen.goto(pen.xcor(), pen.ycor() + 100)  # Posición para los pétalos
    for _ in range(6):  # Dibuja 6 pétalos
        dibujar_petalo()
        pen.left(60)  # Gira para el siguiente pétalo
    pen.penup()
    pen.goto(pen.xcor() - 8, pen.ycor() ) # Posición para el centro
    pen.pendown()
    dibujar_centro()  # Dibuja el centro de la flor

# Función para dibujar el ramo:
def dibujar_ramo():
    pen.penup()
    pen.goto(120, -10)  # Posición del ramo
    pen.pendown()
    pen.color("lightpink")
    pen.begin_fill()
    pen.setheading(180)  # 180 para que la base del triángulo apunte hacia las bases de los tallos
    for _ in range(3):
        pen.forward(240)  # Lados del triángulo
        pen.left(120)
    pen.end_fill()

def dibujar_corazon(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    
    pen.setheading(0)  
    pen.left(140)
    pen.forward(size)  # Parte inferior del corazón
    pen.circle(-size // 2, 200)  # Ajusta la curva
    pen.left(120)
    pen.circle(-size // 2, 200)  # Ajusta la curva
    pen.forward(size)  # Parte inferior del corazón
    
    pen.end_fill()
    pen.setheading(0)  # Restablece la dirección

# Función para escribir el título
def escribir_titulo():
    pen.penup()
    pen.goto(14, 180) # Posición desde donde empieza a escribir
    pen.pendown()
    pen.color("Red")
    pen.write("Por más primaveras juntos <3", align=("center"), font=("Arial", 20, "bold"))

# Función para posicionar turtle para la siguiente flor
def posicionar_flor(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Dibuja el ramo de flores
flor_posiciones = [(-60, 50), (0, 80), (60, 50)]  # Posiciones para las flores
for posicion in flor_posiciones:
    posicionar_flor(*posicion)
    dibujar_flor()

# Dibuja el ramo y los detalles
dibujar_ramo()
dibujar_corazon(0, -120, 40)  # Ajusta la posición y tamaño del corazón
escribir_titulo()

# Finaliza el dibujo
pen.hideturtle()

# Finaliza el dibujo
turtle.done()
