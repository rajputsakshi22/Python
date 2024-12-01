import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.color("green")
t.pensize(2)
t.speed("fastest")

# Position the turtle
t.left(90)
t.penup()
t.backward(100)
t.pendown()

# Tree function
def tree(branch_length):
    if branch_length < 10:
        t.color("orange")
        t.circle(2)  # Draw leaves
        t.color("green")
        return
    else:
        t.forward(branch_length)
        t.color("brown")
        
        t.left(30)
        tree(branch_length * 0.7)  # Left branch
        
        t.right(60)
        tree(branch_length * 0.7)  # Right branch
        
        t.left(30)
        t.backward(branch_length)

# Draw the tree
tree(100)

# Finish
turtle.done()
