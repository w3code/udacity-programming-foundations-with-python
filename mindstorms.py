import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_line(some_line):
    for i in range(1, 4):
        #some_line.right(90)
        some_line.forward(100)

def draw_art():
    # Open the canvas-window
    window = turtle.Screen()
    window.bgcolor('blue')

    # Create the turtle Brad - Draws a square
    brad = turtle.Turtle() # Turtle is a class, brad is an instance or object of this class
    brad.shape('circle')
    brad.color('yellow')
    brad.speed(50)

    for i in range(1, 37): # The loop runs 36 times
        draw_square(brad)
        brad.right(10)

    for i in range(1, 2):
        draw_line(brad)


    window.exitonclick()

draw_art()
