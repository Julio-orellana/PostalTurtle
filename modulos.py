"""

INTEGRANTES: MARCO DIAZ, JULIO ORELLANA
EJERCICIO: POSTAL CON TURTLE
DESCRIPCION DEL PROYECTO: SE GENERARA UN PAISAJE DEL LADO IZQ DE EL CANVAS Y EL LADO DERECHO TENDRA UN MENSAJE PARA INCENTIVAR
                            EL TURISMO EN GUATEMALA Y DE QUIEN Y PARA QUIEN ESTA DIRIGIDA LA POSTAL.

--------------------------------------------------------------------------------------------------------------------------------------

Archivo principal del programa en el cual se incluiran todas las funciones, metodos, bucles,
escrituras, documentaciones, solicitudes, elementos, importaciones y
asignaciones de variables que se requieran para la realización del mismo.

Es decir archivo de "BACK-END"

"""

#Inicio del programa


#Importar librerias

import turtle
import random
import math


#Definir Turtle como t

t = turtle.Turtle()


#Asignar velocidad a t

t.speed(0)


"""

INSTRUCCIONES DE USO PARA LA LIBRERIA TURTLE:

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

#Inicio de funciones del programa

#Funcion para dibujar un rectangulo

def rectangle(height,base):
    for r in range(2):
        t.forward(base)
        t.right(90)
        t.forward(height)
        t.right(90)

#Funcion para dibujar un ovalo

def ovalo (radio, angle):
    t.seth(320)
    x=2
    for o in range(2):
        t.circle(radio, 90)
        t.forward(x)
        t.circle(radio//angle, 90)
        t.forward(x*20)

#Funcion para dibujar un cuadrado

def square (height, base):
    for s in range(2):
        t.forward(base)
        t.right(90)
        t.forward(height)
        t.right(90)

#Funcion para dibujar un triangulo

def triangle (height):
    t.left(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.right(120)
    t.forward(height)

#Funcion para dibujar una montaña

def mountain(mRange, height):
    for m in range(mRange):
        t.left(60)
        t.forward(height)
        t.right(120)
        t.forward(height)
        t.left(60)

#Funcion para dibujar la linea que divide el lienzo

def line (lenght):
    t.left(90)
    t.forward(lenght)
    t.right(180)
    t.forward(lenght*2)

#Funcion para dibujar el nuevo lienzo en el que se trabajara

def lienzo ():
    t.width(8)
    line(300)
    t.left(90)
    t.penup()
    t.goto(-600, 300)
    t.pendown()
    rectangle(600, 1200)
    t.width(5)

#Funcion para dibujar nube de la izquierda

def cloud():
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.goto(-510, 180)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-535, 215)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-549, 172)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-492, 220)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-465, 190)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.pencolor("black")

#Funcion para dibujar Nube de la derecha

def cloud2():
    t.pencolor("white")
    t.fillcolor("white")
    t.penup()
    t.goto(-110, 180)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-135, 215)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-149, 172)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-92, 220)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.goto(-65, 190)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.pencolor("black")

#Funcion para dibujar el sol

def sun():
    
    #Base del sol

    t.pencolor("yellow")
    t.penup()
    t.goto(-60, 300)
    t.pendown()
    t.fillcolor("yellow"), t.begin_fill()
    t.right(90)
    t.circle(60//2, 180)
    t.end_fill()

    #Fin de base del sol

    #Inicio de dibujo de rayos solares

    t.pencolor("red") 
    t.penup()
    t.goto(-59, 290)
    t.left(70)
    t.pendown()
    t.forward(12)
    t.penup()
    t.goto(-57, 280)
    t.left(30)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(-50, 273)
    t.left(60)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(-35, 268)
    t.left(15)
    t.pendown()
    t.forward(13)
    t.penup()
    t.goto(-20, 270)
    t.left(15)
    t.pendown()
    t.forward(15)
    t.penup()
    t.goto(-10, 275)
    t.left(25)
    t.pendown()
    t.forward(12)
    t.pencolor("black")
    
    #Fin de rayos solares

#Funcion para dibujar las bases del muelle

def muelle():
    t.pencolor("black"), t.fillcolor("#ba5225")
    t.penup()
    t.goto(-587, -210)
    t.pendown()
    t.begin_fill()
    for i in range(10):
            rectangle(84, 20)
            t.pendown()
            b=i*20
            c = 15
            t.goto(-584+b+c-i,-210+i)
    t.end_fill()

#Funcion de Menu Principal

def menu ():

    #Solicitamos al usuario que desea hacer

    op = str(input("Desea enviar una carta?: s/n: "))

    #Inicio del bucle

    while True: #Programa Principal

    #Configuracion del menu

        #Si la opcion es verdadera

        if op == "s":
            name1 = str(input("Ingrese el nombre del remitente: "))
            name2 = str(input("Ingrese el nombre del destinatario: "))
            t.clear()
            t.penup()
            t.goto(0,0)
            t.pendown()
            lienzo()
            t.hideturtle()
            #Prueba de dibujo y escritura en el nuevo lienzo de trabajo
            t.penup()
            t.goto(20, 150)
            t.pendown()
            t.write(f"DE: {name1.upper()}", font=('Arial',25))
            t.penup()
            t.goto(20, 75)
            t.pendown()
            t.write(f"PARA: {name2.upper()}", font=('Arial',20 ))
            t.penup()

            t.pendown()
            t.penup()
            t.goto(20,-200)
            t.write("¡Descubre la magia de los volcanes en Guatemala!\n Bienvenidos a una tierra donde la naturaleza se despierta con fuerza y\n ​​belleza incomparable:\n ¡Guatemala! Hogar de algunos de los volcanes más impresionantes del mundo,\n te invitamos a explorar y maravillarte con la majestuosidad de estos gigantes de fuego.\n Desde el místico Volcán Pacaya,\n donde podrás caminar sobre lava solidificada,\n hasta el imponente Volcán de Agua,\n que domina el paisaje con su silueta majestuosa,\n cada volcán en Guatemala ofrece una experiencia única e inolvidable.\n Te esperamos con los brazos abiertos y\n el corazón lleno de pasión por compartir nuestra tierra con el mundo. \n¡Ven y únete a la experiencia de Guatemala, donde la naturaleza te dejará sin aliento!", font=('Arial',14,'normal'))
            t.pendown()
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

            #Dibujando el muelle

            #Dibujando la pasarela del muelle
            t.penup()
            t.goto(-600,-150)
            t.pendown()
            t.fillcolor("#000000")
            for i in range(20):
                
                square(60,20)
                t.pendown()
                b=i*10
                t.goto(-580+b-i,-150+i)
            
            #Dibujando la base del muelle

            muelle()

            #Fin del dibujo del muelle
            
 
            #Dibujando las montañas

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
            t.end_fill

            #Fin del dibujado de montañas

            #Dibujar el Volcan

            t.penup()
            t.goto(-500,-100)
            t.pendown()
            t.fillcolor("#4E2728")
            t.begin_fill()
            mountain(1,400)
            t.end_fill()

            #Dibujando las nubes

            cloud()
            cloud2()

            #Dibujando el sol

            sun()

            #Reiniciar la solicitud para saber si desea reutilizar el programa

            op = str(input("Desea enviar otra carta?: s/n: "))

            #Preparar el canvas de nuevo por si se reutiliza el programa

            t.clear()
            t.seth(0)
            t.penup()
            t.goto(0,0)
            t.pendown()
    
        #Fin de programa principal

        #Definir cuando finaliza el bucle
        #Si la opcion es falsa:

        elif op == "n":#Se ejecuta si la opcion del usuario es que no desea usar el programa "n"
            print("\nSaliendo...\n")
            turtle.bye()#Llamamos a la funcion bye para salir de la ventana emergente.
            break #Se utiliza el break para indicar a python que el programa se finaliza por complet si la seleccion es n.

        #Fin de definicion de punto de acabado del bucle

        #Configurar menu si la opcion es invalida

        else: #Si la opcion del usuario no es valida, es decir no es "s" o "n".
            print("\nError, entrada no valida.\nPor favor escriba s si desea enviar una carta o, n si desea salir\n")
            op = str(input("Desea enviar una carta?: s/n: "))#Pedimos al usuario que escoja una opcion valida
        #Fin de configuracion del menu

    #Fin de creacion de funciones
#Fin del programa