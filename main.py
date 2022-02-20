import turtle as t
import random

# assign the class from turtle module to tim
tim = t.Turtle()

colors = ["orange red", "red", "coral", "dark orange", "gold", "black"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):    # Will draw triangle through decagon (3-10 sided shapes)
    tim.color(random.choice(colors))    # Will select a random color each timea shape is drawn
    draw_shape(shape_side_n)        # References our draw shape function




