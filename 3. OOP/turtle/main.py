# import turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

# 버튼을 눌를 때만 사라지도록 만든다.
my_screen.exitonclick()
