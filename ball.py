import turtle

class Ball:
    def __init__(self):
        pass

    def draw_ball(self, color, size, x, y):
        # draw a circle of radius equals to size at x, y coordinates and paint it with color
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y-size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()

    def move_ball(self, i, xpos, ypos, vx, vy, dt):
        # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
        xpos[i] += vx[i]*dt
        ypos[i] += vy[i]*dt


    def update_ball_velocity(self, i, xpos, ypos, vx, vy, canvas_width, canvas_height, ball_radius):
        # if the ball hits the side walls, reverse the vx velocity
        if abs(xpos[i]) > (canvas_width - ball_radius):
            vx[i] = -vx[i]

        # if the ball hits the ceiling or the floor, reverse the vy velocity
        if abs(ypos[i]) > (canvas_height - ball_radius):
            vy[i] = -vy[i]