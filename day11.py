from turtle import *
import random

# Set up the screen
bgcolor("midnight blue")
title("Night Sky with Stars and Moon")
speed(0)

# Function to draw the stars with flickering effect
def draw_star(size, color, x, y):
    penup()
    goto(x, y)
    pendown()
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

# Function to draw the moon with a glow effect
def draw_moon():
    penup()
    goto(100, 100)
    pendown()
    # Draw main moon
    pencolor("white")
    fillcolor("light yellow")
    begin_fill()
    circle(50)
    end_fill()

    # Adding a crescent effect
    penup()
    goto(120, 120)
    pendown()
    bgcolor("midnight blue")
    fillcolor("midnight blue")
    begin_fill()
    circle(40)
    end_fill()

    # Adding moon glow effect
    penup()
    goto(100, 100)
    pendown()
    pencolor("light yellow")
    fillcolor("light yellow")
    begin_fill()
    circle(60)
    end_fill()

# Function to draw stars randomly with a flickering effect
def draw_stars():
    colors = ["white", "light yellow", "light blue"]
    for _ in range(30):  # Increased number of stars
        size = random.randint(10, 25)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_star(size, random.choice(colors), x, y)

# Function to draw clouds
def draw_cloud(x, y):
    penup()
    goto(x, y)
    pendown()
    fillcolor("white")
    begin_fill()
    for _ in range(6):
        circle(random.randint(15, 30))
        penup()
        forward(random.randint(20, 40))
        pendown()
    end_fill()

# Function to draw shooting stars with animation
def draw_shooting_star():
    penup()
    x = random.randint(-400, 400)
    y = random.randint(100, 300)
    goto(x, y)
    pendown()
    pencolor("white")
    width(2)
    for _ in range(20):
        forward(10)
        right(10)
    width(1)

# Function to write a message
def write_message():
    penup()
    goto(-150, -200)
    pendown()
    pencolor("white")
    style = ("Arial", 24, "bold")
    write("Gazing at the Night Sky!", font=style, align="center")

# Drawing the sky gradient (from dark blue to light blue near the horizon)
def draw_gradient():
    for i in range(300):
        r = i / 300.0
        g = r / 2.0
        b = 1 - r
        bgcolor(r, g, b)

# Function for shooting stars animation
def animate_shooting_stars():
    for _ in range(5):  # Add 5 shooting stars with animation
        draw_shooting_star()

# Function to animate flickering stars
def animate_flickering_stars():
    for _ in range(5):  # Flicker effect for 5 stars
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(10, 25)
        color = random.choice(["white", "light yellow", "light blue"])
        draw_star(size, color, x, y)
        penup()
        time.sleep(random.uniform(0.1, 0.5))  # Simulating flickering

# Draw background gradient
draw_gradient()

# Draw the moon
draw_moon()

# Draw the stars
draw_stars()

# Draw shooting stars with animation
animate_shooting_stars()

# Draw some clouds in the sky
for _ in range(5):
    draw_cloud(random.randint(-300, 300), random.randint(-100, 100))

# Animate flickering stars
animate_flickering_stars()

# Write the message
write_message()

hideturtle()
done()
