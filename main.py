print ("hello world")
import turtle

# Function to draw a heart
def draw_heart():
    turtle.color('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

# Set up the turtle
turtle.speed(2)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Draw the word "love"
turtle.write("alif kontol", align="center", font=("Arial", 24, "normal"))

# Move to a new position for the heart
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Draw a heart
draw_heart()

# Close the turtle graphics window on click
turtle.exitonclick()
