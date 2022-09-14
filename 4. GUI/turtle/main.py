from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# turtle 로 4각형 만들기
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# turtle 로 점선 만들기
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# turtle 로 다각형 만들기
for _ in range(3, 11):
    angle = 360 / _
    for _ in range(_):
        timmy.forward(100)
        timmy.right(angle)


screen = Screen()
screen.exitonclick()
