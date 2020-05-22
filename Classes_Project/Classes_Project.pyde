# Class contains all the logic for the square
#     Keypressed (W-A-S-D)
#     All the pretty colors and drawing

# Setup!
#     All the basic setup funcitons
#     Background
#     Colors and shit.... idk whatver 

# Draw!
#     Loop where you call your class and make it do stuff

# Class functions:
#     move
#     draw
#     detect_key

# self.x = 340
# self.y = 323

class Doggo():
    def __init__(self, name):
        self.name = name
        
    def return_name(self):
        print(self.name)
        

dg = Doggo('OwO')
ep = Doggo('UwU')
dg.return_name()
ep.return_name()
# ------------------------------ 
# |                            | 
# |       @ <moves with wasd>  |
# |                            |        
# |                            | 
# |                            | 
# |                            | 
# |                            | 
# |                            | 
# |                            | 
# |                            | 
# ------------------------------
