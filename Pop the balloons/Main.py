import turtle
import random
import time
spawn_interval=2

paper=turtle.Screen()
paper.bgcolor("black")
paper.tracer(0)

balloons=[]

score=0
score_display=turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.up()
score_display.goto(-300,300)
score_display.write("score"+ str(score),font=("Arial",16))

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

def circle():
    balloon=turtle.Turtle()
    balloon.shape("circle")
    colors=["white","blue","green","purple","red","yellow","orange"]
    balloon.color(random.choice(colors))
    balloon.up()
    balloon.goto(random.randint(-350,350),370)
    balloon.speed=random.uniform(1,3)
    balloons.append(balloon)
lastspawntime=time.time()
while True:
    paper.update()
    current_time=time.time()
    if current_time-lastspawntime>spawn_interval:
        circle()
        lastspawntime=current_time
    
    for i in balloons[:]:
        i.sety(i.ycor()-i.speed)
        if i.ycor()<-300:
            balloons.remove(i)
            i.hideturtle()

        if i.distance(dart)<30:
            balloons.remove(i)
            i.hideturtle()
            score=score+1
            score_display.clear()
            score_display.write("score"+ str(score),font=("Arial",16))

    time.sleep(0.02)
        
turtle.done()
