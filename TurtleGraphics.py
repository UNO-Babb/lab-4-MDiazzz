#TurtleGraphics.py
#Name: Michelle Diaz
#Date:9/21/2025
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(bob, size):
    for i in range(4):
        bob.forward(size)
        bob.right(90)
        
def drawpolygon(bob,sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillcorner(alice,corner):
    drawSquare(alice,100)
    if corner ==1:
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
    elif corner ==2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()
        
    elif corner ==3:
        alice.right(90)
        alice.forward(100)
        alice.left(180)
        alice.begin_fill()
        drawSquare(alice,50)
        alice.end_fill()

def main():
    bob = turtle.Turtle()
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    drawpolygon(bob,5)
    
    # drawPolygon(myTurtle, 8) #draws an octogon
    drawpolygon(bob,8)
    
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    fillcorner(bob,2)
    
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    fillcorner(bob,3)
    
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
    

