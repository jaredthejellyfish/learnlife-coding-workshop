x = 250
y = 250

step_size = 4

def setup():
    size(500, 500)
    background(0)

def draw():
    global x, y
    
    noStroke()
    fill(255, 0, 0)
    ellipse(x, y, 10, 10)
    # point(x, y)
    
    n = floor(random(4))
    
    if (n == 0):
        x = x + step_size
    elif (n == 1):
        x = x - step_size
    elif (n == 2):
        y = y + step_size
    else:
        y = y - step_size
