import turtle
import random

paper=turtle.Screen()
paper.bgcolor("black")

dart=turtle.Turtle()
dart.shape("triangle")
dart.color("white")
dart.setheading(90)
dart.up()
dart.goto(0,-300)

def move_right():
    x=dart.xcor()+30
    if x<390:
        dart.setx(x)
    
def move_left():
    x=dart.xcor()-30
    if x>-390:
        dart.setx(x)

paper.listen()
paper.onkey(move_right,"d")
paper.onkey(move_left,"a")


turtle.done()
