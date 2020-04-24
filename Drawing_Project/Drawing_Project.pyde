# The setup function is run once at the beginning
def setup():
    # Create a canvas of size 800 x 800
    size(800, 500)
    # Set the background color to white
    background(255, 255, 255)
    # Color the shapes black
    fill(0)
    # No shape outline
    noStroke()

# The draw function is run every frame of animation
def draw():
    # Draw a circle at the mouse position
    ellipse(mouseX, mouseY, 10, 10)

# When a key is pressed, this function will be called
def keyPressed():
    # Check for specific keys and change the shape color accordingly
    # If the key is 'c', clear the canvas
    if key == 'r':
        fill(255, 0, 0)
    elif key == 'g':
        fill(0, 255, 0)
    elif key == 'b':
        fill(0, 0, 255)
    elif key == 'c':
        clear()

# Function that clears the canvas by coloring it white
def clear():
    background(255, 255, 255)
