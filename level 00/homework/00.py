import turtle



# we want to paint a house 

# step1: draw a square

turtle.speed(3)
turtle.width(3)
turtle.color("red")
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.end_fill()
# end of square

#drawing a door

turtle.forward(70)
turtle.color("black")
turtle.begin_fill()
turtle.left(90)
turtle.forward(80) #haight of the door
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(70)
turtle.end_fill()


turtle.penup()
turtle.goto(200,200)
turtle.pendown()


turtle.color("blue")
turtle.begin_fill()
turtle.right(220)
turtle.forward(130)
turtle.left(80)
turtle.forward(130)
turtle.end_fill()

# end of roof

#drawing  first window

turtle.color("pink")
turtle.begin_fill()
turtle.penup()
turtle.goto(10,110)
turtle.left(140)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()

#end first window
turtle.color("pink")
turtle.begin_fill()
turtle.penup()
turtle.goto(140,110)
turtle.pendown()
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.end_fill()








turtle.exitonclick()