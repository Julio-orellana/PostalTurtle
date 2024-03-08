"""
Integrantes: Marco Díaz & Julio Orellana
Ejercicio Estructuras cíclicas
Este proyecto creará una postal con una imagen en el lado izquierdo y un texto del lado derecho.
"""
#Importar Modulos
import turtle
#Definir t
t = turtle.Turtle()
#Asignar velocidad a t
t.speed(20)

"""
● forward(distancia): avanza una determinada cantidad de píxeles, indicado en distancia.
● backward(distancia): retrocede una determinada cantidad de píxeles, indicada en distancia.
● left(ángulo): gira hacia la izquierda un determinado ángulo en grados.
● right(ángulo): gira hacia la derecha un determinado ángulo en grados.
● penup(): levanta el lapicero, permitiendo a la tortuga moverse sin pintar.
● pendown(): baja el lapicero de la tortuga (por defecto está abajo, por lo que la tortuga pinta cuando se mueve).
● circle(radio): dibuja un círculo dado un radio.
● color(color): cambia el color del lapicero y de relleno al especificado en color.
● width(dimensión): cambia el tamaño del grosor de la punta del lapicero, conforme al valor dado en dimensión.
● goto(x,y) | setpos(x,y): traslada al lapicero a la posición en el plano determinada por (x, y)
"""

#Creacion de funciones del programa

#Bibujar un rectangulo
def rectangle(height,base):
    for r in range(2):
        t.forward(base)
        t.right(90)
        t.forward(height)
        t.right(90)
#Dibujar un ovalo
def ovalo (radio, angle):
    for o in range(2):
        t.circle(radio, 90)
        t.circle(radio//angle, 90)
#Dibujar un cuadrado
def square (height, base):
    for s in range(2):
        t.forward(base)
        t.right(90)
        t.forward(height)
        t.right(90)
#Dibujar un triangulo
def triangle (height):
    t.left(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.right(120)
    t.forward(height)
#Dibujar una montaña
def mountain(mRange, height):
    mRange = 2 #Cuantas montañas necesitamos
    for m in mRange:
        t.left(60)
        t.forward(height)
        t.right(120)
        t.forward(height)
        t.left(60)
#Menu Principal
def menu ():
    op = str(input("Desea enviar una carta?: s/n "))
    while True:
        if op == "s":
            name1 = str(input("Ingrese el nombre del remitente: "))
            name2 = str(input("Ingrese el nombre del destinatario: "))
            lienzo()
            #Prueba de dibujo y escritura en el nuevo lienzo de trabajo
            t.penup()
            t.goto(200, 150)
            t.pendown()
            t.write(name1)
            t.write(name1)
            t.penup()
            t.goto(-200, 150)
            t.pendown()
            square(100, 100)
            turtle.done()
            op = str(input("Desea enviar otra carta?: s/n: "))
        elif op == "n":
            print("\nSaliendo...\n")
            break
        else: 
            print("Error")
            op = str(input("Desea enviar una carta?: s/n: "))
#Linea que divide el lienzo
def line (lenght):
    t.left(90)
    t.forward(lenght)
    t.right(180)
    t.forward(lenght*2)
#Dibujar el nuevo lienzo en el que se trabajara
def lienzo ():
    t.width(5)
    line(300)
    t.left(90)
    t.penup()
    t.goto(-600, 300)
    t.pendown()
    rectangle(600, 1200)

"""t.seth(-45)
ovalo(80,3)
t.seth(0)
mountain(altura)
rectangle(altura, base)
square(altura, base)
triangle(altura)
ovalo(radio, angulo de curvatura)
""" 
