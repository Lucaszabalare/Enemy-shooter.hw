# no enemies allowed
import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 450

TITLE = "Enemy Madness"
message = ""
ph = 10


dog = Actor("enemy")

def draw():
    screen.clear()
    screen.fill(color = "brown")
    dog.draw()
    screen.draw.text(message,center = (300,20),fontsize = 30,color = "red")

def enemy_place():
    dog.x = randint(50,450)
    dog.y = randint(50,400)

def on_mouse_down(pos):
    global message
    if dog.collidepoint(pos):
        message = "Enemy shot!"
        enemy_place()
    else:
        message = "Enemy missed!"

enemy_place()
pgzrun.go()