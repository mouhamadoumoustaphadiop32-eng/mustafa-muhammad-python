import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

couleurs = ["cyan", "magenta", "yellow", "orange"]

def carre(taille):
    for i in range(4):
        t.forward(taille)
        t.left(90)

for i in range(36):
    t.color(couleurs[i % len(couleurs)])
    carre(100)
    t.left(10)

turtle.done()