# x and y store the position of the ellipse
x = 0
y = 0

# the x and y speed of the ellipse
x_speed = 5
y_speed = 5

# the dimensions of the ellipse
ellipse_width = 100
ellipse_height = 50

# setup gets called once
def setup():
    # the global keyword must be used as x and y are getting changed and they are global vars
    global x, y
    size(1280, 720)
    x = width/2
    y = height/2

# draw gets called once per frame
def draw():  
    global x, y
  
    background(0)
    noStroke()
    # draw the ellipse at the x and y position with the specified dimensions
    ellipse(x, y, ellipse_width, ellipse_height)
    
    # check if the ellipse has collided with the boundaries
    check_edges()
    
    # update the ellipse position
    x += x_speed
    y += y_speed
    
# this function checks if the ellipse collides with the edges of the screen and reverses the ellipse's direction
def check_edges():
    global x_speed, y_speed
    if x + ellipse_width/2 > width or x - ellipse_width/2 < 0:
        x_speed = x_speed * -1
        fill(random(255), random(255), random(255))
    if y + ellipse_height/2 > height or y - ellipse_height/2 < 0:
        y_speed = y_speed * -1
        fill(random(255), random(255), random(255))
