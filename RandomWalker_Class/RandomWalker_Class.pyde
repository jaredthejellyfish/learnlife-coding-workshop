class RandomWalker:
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
    
    def display(self):
        fill(self.r, self.g, self.b, 50)
        noStroke()
        ellipse(self.x, self.y, 25, 25)
    
    def move(self):
        dx = random(-5, 5)
        dy = random(-5, 5)
        self.x += dx
        self.y += dy
       
list_of_walkers = [RandomWalker(250, 250, 255, 0, 0), RandomWalker(100, 100, 0, 255, 0), RandomWalker(400, 400, 0, 0, 255)]

def setup():
    size(500, 500)
    background(0)

def draw():
    # use a for loop to display and move each RandomWalker in the list
    for x in list_of_walkers:
        x.display()
        x.move()
    
