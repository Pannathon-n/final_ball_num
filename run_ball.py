import turtle
from ball import Ball
from seven_segments_proc import Number
import random

class Play:
    def __init__(self):
        self.num_balls = 5
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        print(self.canvas_width, self.canvas_height)
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []

        # create random number of balls, num_balls, located at random positions within the canvas; each ball has a random velocity value in the x and y direction and is painted with a random color
        for i in range(self.num_balls):
            self.xpos.append(random.uniform(-1*self.canvas_width + self.ball_radius, self.canvas_width - self.ball_radius))
            self.ypos.append(random.uniform(-1*self.canvas_height + self.ball_radius, self.canvas_height - self.ball_radius))
            self.vx.append(10*random.uniform(-1.0, 1.0))
            self.vy.append(10*random.uniform(-1.0, 1.0))
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def draw_border(self):
        turtle.penup()
        turtle.goto(-self.canvas_width, -self.canvas_height)
        turtle.pensize(10)
        turtle.pendown()
        turtle.color((0, 0, 0))
        for i in range(2):
            turtle.forward(2*self.canvas_width)
            turtle.left(90)
            turtle.forward(2*self.canvas_height)
            turtle.left(90)

dt = 0.7 # time step
Tom = turtle.Turtle()
tom_color = (255, 0, 0)
test = Number(Tom, tom_color)
delay_in_seconds = 0.01
test_b = Ball()
play = Play()
counter = 0
frame_count = 0
while (True):
    turtle.clear()
    play.draw_border()
    for i in range(play.num_balls):
        test_b.draw_ball(play.ball_color[i], play.ball_radius, play.xpos[i], play.ypos[i])
        test_b.move_ball(i, play.xpos, play.ypos, play.vx, play.vy, dt)
        test_b.update_ball_velocity(i, play.xpos, play.ypos, play.vx, play.vy, play.canvas_width, play.canvas_height, play.ball_radius)
    test.clear() 
    test.draw(Tom, counter)
    frame_count += 1
    if frame_count >= 20:
        counter = (counter + 1) % 10
        frame_count = 0
    test.my_delay(delay_in_seconds)
    
    turtle.update()

# hold the window; close it by clicking the window close 'x' mark
turtle.done()