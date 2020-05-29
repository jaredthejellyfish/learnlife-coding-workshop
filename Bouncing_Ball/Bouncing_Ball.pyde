# This is the ball class that handles everything related to Balls
class Ball:
    # The __init__ method is used to initialize class variables
    def __init__(self, position, velocity, acceleration):
        # Each ball has a position, velocity and acceleration
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
    
    # The display method handles drawing the ball
    def display(self):
        noStroke()
        fill(255, 0, 0)
        ellipse(self.position.x, self.position.y, 50, 50)

    # The move method handles moving the Ball
    def move(self):
        # Velocity changes according to acceleration
        self.velocity.add(self.acceleration) 
        # Position changes according to velocity
        self.position.add(self.velocity)
        # Reset acceleration
        self.acceleration.mult(0)
    
    # The add_force method adds a force to the acceleration of the Ball
    def add_force(self, force):
        self.acceleration.add(force)
    
    # check_ground checks if the ball falls off the bottom of the screen.
    # if it is off the screen, the ball bounces up
    def check_ground(self):
        if self.position.y > height:
            self.velocity.y *= -1
            self.position.y = height

gravity = PVector(0, 1)
# creating a new ball at position 250, 250 with velocity and acceleration 0
b = Ball(PVector(250, 250), PVector(0, 0), PVector(0, 0))

def setup():
    size(500, 500)
 
def draw():
    background(0)
    
    b.display()
    b.move()
    b.add_force(gravity)
    b.check_ground()
