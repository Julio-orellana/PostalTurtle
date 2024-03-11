"""
Integrantes: Marco Díaz & Julio Orellana
Ejercicio Estructuras cíclicas
Este proyecto creará una postal con una imagen en el lado izquierdo y un texto del lado derecho.
"""
#Importar Modulos
import turtle
import random
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
    t.seth(320)
    x=2
    for o in range(2):
        t.circle(radio, 90)
        t.forward(x)
        t.circle(radio//angle, 90)
        t.forward(x*20)
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
        #Cuantas montañas necesitamos
    for m in range(mRange):
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
            t.clear()
            t.penup()
            t.goto(0,0)
            t.pendown()
            lienzo()
            #Prueba de dibujo y escritura en el nuevo lienzo de trabajo
            t.penup()
            t.goto(200, 150)
            t.pendown()
            t.write(name1)
            t.write(name2)
            t.penup()
            t.goto(-599, 300)
            t.fillcolor("#285a80")
            t.begin_fill()
            t.pendown()
            square(400, 600)
            #aqui va el cielo
            t.end_fill()
            t.penup()
            t.goto(-600,-100)
            t.pendown()
            t.fillcolor("#243d4f")
            t.begin_fill()
            square(200,600)
            t.end_fill()
            #aqui va el lago

            t.penup()
            t.goto(-600,-150)
            t.pendown()
            t.fillcolor("#000000")
            for i in range(20):
                
                square(60,20)
                t.pendown()
                b=i*10
                t.goto(-580+b-i,-150+i)

            #muelle
 
            #montañas empiezan aqui
            t.color("black")
            t.penup()
            t.goto(-600,-100)
            t.pendown()
            t.fillcolor("#58564a")
            t.begin_fill()
            mountain(4,150)
            t.end_fill()
            t.penup()
            t.goto(-600,-100)
            t.pendown

            t.fillcolor("#243138")
            t.begin_fill()
            t.penup()
            t.color("black")
            t.fillcolor("#35484e")
            t.begin_fill()
            mountain(6,100)
            t.end_fill()
            t.fillcolor("")

            t.fillcolor("#ffffff")
            t.begin_fill()
            cloud(-50, 0, 50, 10)
            t.end_fill
            #montañas terminan aquí
            #creo que cuando "pones el mismo color color encima de otro se cancelan"
            t.penup()
            t.goto(-500,-100)
            t.pendown()
            t.fillcolor("#35484e")
            t.begin_fill()
            mountain(1,400)
            t.end_fill()
            
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
#Dibujar nubes
def cloud(x,y,radio,n):
    t.penup()
    #Posicion en eje x & posicion en eje y
    t.goto(x,y)
    t.pendown()
    #Radio de la basa de la nube
    t.circle(radio)
    for c in range(n):#Dibujar las orillas de la nube, n es el rango de cuantas necesitamos
        t.penup()
        t.goto(random.uniform(-radio, radio), random.uniform(0, radio))
        t.pendown()
        t.circle(random.uniform(10,30))



"""t.seth(-45)
ovalo(80,3)
t.seth(0)
mountain(altura)
rectangle(altura, base)
square(altura, base)
triangle(altura)
ovalo(radio, angulo de curvatura)
""" 
menu()
t.exitonclick()