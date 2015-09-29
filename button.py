#button.py

# This button class was written written by John Zelle in the book 
# "Python Programming: An Introduction to Computer Science" (Franklin, Beedle & Associates)

from graphics import *
class Button:
    """ A button is a labeled rectangel in a window. It is activated or deactivated with the 
    activate() and deactivate() methods. The clicked(p) method returns true if the button 
    is active and p is inside it. """
    
    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular botton. """
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.x = x
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.color = 'lightgray'
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        self.count = 0
        
    def getX(self):
        """ Returns the x value of the center of the button. """
        return self.x
    
            
    def clicked(self, p):
        """ Returns true if button active and p is inside. """
        return self.active and \
            self.xmin <= p.getX() <= self.xmax and \
            self.ymin <= p.getY() <= self.ymax
    
    def updateCount(self):
        """ Increases count by one every time a button is pressed.
        For the purposes of our Connect 4 game, a button is 
        deactivated after it has been clicked 6 times. """
        
        self.count += 1
        if self.count >= 6: 
            self.deactivate()   
                
    def getLabel(self):
        """ Returns the label string of this button. """
        return self.label.getText()
    
    def setFill(self, color):
        """ Sets the fill of a button to a certain color. """
        self.rect.setFill(color)
        self.color = color
    
    def getColor(self):
        """ Returns the color of the button. """
        return self.color
    
    def activate(self):
        """ Sets this button to active. """
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        
    def deactivate(self):
        """ Sets this button to inactive. """
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
