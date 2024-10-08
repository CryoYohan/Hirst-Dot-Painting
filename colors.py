from turtle import Turtle,Screen
import turtle
from random import choice
class HirstPainting:


    def __init__(self):
        self.tim = Turtle()
        self.tim.hideturtle()
        self.screen = Screen()
        self.screen.colormode(255)
        self.rbg_colors = [(203, 165, 108), (152, 74, 48), (52, 93, 124), (170, 153, 41), (223, 202, 136), (137, 32, 21),
                      (132, 163, 185), (47, 121, 88), (198, 91, 72), (15, 99, 73), (70, 47, 39), (147, 179, 148),
                      (98, 73, 75), (162, 142, 157), (234, 175, 164), (55, 46, 49), (184, 205, 172), (24, 81, 87),
                      (38, 61, 74), (142, 22, 25), (85, 146, 126), (45, 65, 85), (175, 91, 94), (214, 177, 183),
                      (18, 70, 64), (109, 125, 151)]
        self.TURTLE_XCOR = -320.00
        self.turtle_ycor_var = -260.00

    def random_color(self):
        return choice(self.rbg_colors)

    def dot_painting(self, size_of_dot):
        self.tim.penup()
        self.tim.setpos(self.TURTLE_XCOR,self.turtle_ycor_var)
        for _ in range(14):
            for _ in range(14):
                self.tim.dot(size_of_dot, self.random_color())
                self.tim.fd(50)
            self.turtle_ycor_var += 50
            self.tim.setpos(self.TURTLE_XCOR,self.turtle_ycor_var )
            print(f"Current Y Coordinates: {self.turtle_ycor_var}")
        self.screen.exitonclick()

    def spirograph(self, size_of_gap):
        turtle.title('Spirogram')
        turtle.textinput('NIM0','Enter name: ')
        for _ in range(int(360/size_of_gap)):
            self.tim.color(self.random_color())
            self.tim.circle(100)
            self.tim.setheading(self.tim.heading() + size_of_gap)
        self.screen.exitonclick()





