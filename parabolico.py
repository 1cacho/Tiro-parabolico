from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Aumentar la velocidad del proyectil (multiplicador mayor)
        speed.x = (x + 200) / 15  # Cambiado de 25 a 15
        speed.y = (y + 200) / 15  # Cambiado de 25 a 15

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    # Aumentar la frecuencia de aparición de balones
    if randrange(30) == 0:  # Cambiado de 40 a 30 (aparecen más seguido)
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Aumentar la velocidad de los balones
    for target in targets:
        target.x -= 1.0  # Cambiado de 0.5 a 1.0 (el doble de rápido)

    if inside(ball):
        # Reducir la gravedad para que el proyectil sea más rápido
        speed.y -= 0.25  # Cambiado de 0.35 a 0.25 (menos gravedad)
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Aumentar la velocidad general del juego reduciendo el intervalo del timer
    for target in targets:
        if not inside(target):
            return

    ontimer(move, 30)  # Cambiado de 50 a 30 (más frames por segundo)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
