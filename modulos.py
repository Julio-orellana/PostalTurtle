import turtle
t=turtle.turtle()

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
def rectangle(height,base):
    a=0
    while a==2:
        t.turtle.setheading(0)
        t.turtle.forward(base)
        t.turtle.right(90)
        t.turtle.forward(height)
        a+=1
def ovalo (height, base):

def circulo (height, base):

def