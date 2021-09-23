"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Chase Byers

This code creates a space themed generative art peice. On a black background, 
different sets of stars travel to randome coordinates to create a unique 
screen each time. 

"""
import turtle
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 1000 # width of panel
h = 1000 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
turtle.speed(50)
turtle.clear()
turtle.goto(0,0)
turtle.speed(20)
turtle.pensize(4)

panel = turtle.Screen().bgcolor("black") 
colorPalette = [(1,31,75),(3,57,108),(0,91,150),(100,151,177),(179,205,224)]
randomLocations = [(0,0), (-100,100),(-120,400),(300,200),(400,500),(-9,-500), (400,-450),(-80,90), (360,-90), (-184.560), (-300,400), (-89,600), (450,560)]
randomLocations2 = [(0,0), (10,-10),(12,-40),(-30,-20),(-40,-50),(9,50), (-20,45),(80,-90), (-30,90), (-18.-50), (-30,40), (-89,60), (-56,-78), (45,56)]

#the loop below chooses 25 different locations and changes the color for each 
#the for loop within the loop draws a star with 5 points
for i in range(25):
    turtle.up()
    turtle.goto(random.choice(randomLocations))
    turtle.color(random.choice(colorPalette))
    turtle.down()
    for i in range(5):
        turtle.forward(200)
        turtle.left(145)


turtle = turtle.Turtle()
turtle.color("yellow")
turtle.pensize(6)
turtle.down()

#the for loop below chooses 12 random locations for 12 circles
for i in range (1,10):
    turtle.up()
    turtle.goto(random.choice(randomLocations2))
    turtle.down()
    turtle.circle(12)
   

turtle.up()
turtle.done()
turtle.clear()
             


# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
