# Connect4.py
# Anna Meyer, Alex Olson, CS111, Fall 2014

from button import *
from graphics import *
from random import *

def drawButtons(window):
    """ Makes and returns a list of all the buttons, each of which correspond
    to a column, and will be used to place tiles on the board. """
    
    button1 = Button(window, Point(50, 50), 30, 30, "1")
    button1.activate()
    button2 = Button(window, Point(100, 50), 30, 30, "2")
    button2.activate()
    button3 = Button(window, Point(150, 50), 30, 30, "3")
    button3.activate()
    button4 = Button(window, Point(200, 50), 30, 30, "4")
    button4.activate()
    button5 = Button(window, Point(250, 50), 30, 30, "5")
    button5.activate()
    button6 = Button(window, Point(300, 50), 30, 30, "6")
    button6.activate()
    
    buttonList = [button1, button2, button3, button4, button5, button6]
    
    return buttonList 
    
def addBoard(window):
    """ Draws the Connect4 grid in the graphics window. """
    
    for i in range(6):
        rect = Rectangle(Point(25+50*i, 325), Point(75+50*i, 75))
        rect.draw(window)
    for i in range(4):
        rect = Rectangle(Point(25, 280 - 40*i), Point(325, 240 - 40*i))
        rect.draw(window)
        
def chooseColor():
    """ This function allows the human player to choose their tile color. The
    color options are purple, red, orange, yellow, light green, green, light blue,
    blue, and white. """
    
    window = GraphWin("", 195, 215)
    
    label = Text(Point(100, 25), 'Choose your Color!')
    label.setSize(17)
    label.draw(window)

    button1 = Button(window, Point(50, 70), 50, 50, "")
    button1.activate()
    button1.setFill(color_rgb(138, 43, 226))
    
    button2 = Button(window, Point(100, 70), 50, 50, "")
    button2.activate()
    button2.setFill(color_rgb(200, 0, 0))
    
    button3 = Button(window, Point(150, 70), 50, 50, "")
    button3.activate()
    button3.setFill(color_rgb(255, 104, 31))
    
    button4 = Button(window, Point(150, 120), 50, 50, "")
    button4.activate()
    button4.setFill(color_rgb(255, 215, 0))
    
    button5 = Button(window, Point(150, 170), 50, 50, "")
    button5.activate()
    button5.setFill(color_rgb(161, 197, 10))
    
    button6 = Button(window, Point(100, 170), 50, 50, "")
    button6.activate()
    button6.setFill(color_rgb(34, 139, 34))
    
    button7 = Button(window, Point(50, 170), 50, 50, "")
    button7.activate()
    button7.setFill(color_rgb(0, 149, 182))
    
    button8 = Button(window, Point(50, 120), 50, 50, "")
    button8.activate()
    button8.setFill(color_rgb(63, 0, 255))
    
    button9 = Button(window, Point(100, 120), 50, 50, "")
    button9.activate()
    button9.setFill('white')
    
    buttonList = [button1, button2, button3, button4, button5, 
                  button6, button7, button8, button9]
    
    # This while loop prevents the program from crashing if the user does 
    # not click on one of the colored buttons
    waiting = True
    while waiting == True:
        p = window.getMouse()
        for button in buttonList:
            if button.clicked(p):
                window.close()
                waiting = False
                return button.getColor()

        
def find4(List):
    """ This function checks for 4-in-a-rows in a given list by using a loop that increases a count 
    for every subsequent tile played by the same player. If count reaches three, it means 
    that there is a 4-in-a-row in the list. If a 4-in-a-row is found, the function returns 
    either 'P' (which means the player won) or 'C' (which means the computer won).
    Otherwise, the function returns False. """
    
    count = 0
    for i in range(len(List)-1):
        if (List[i] == 'P' and List[i + 1] == 'P') or \
        (List[i] == 'C' and List[i + 1] == 'C'):
            count += 1
        else:
            count = 0
            
        if count >= 3:
            return List[i]
        
    return False


def find3(List):
    """ Checks for 3-in-a-rows in a given list by using a loop that increases a count for 
    every subsequent tile played by the same player. If count reaches 2, it means there 
    is a 3-in-a-row in the list. If a 3-in-a-row is found, the function identifies whether 
    it belongs to the player or computer and returns the proper column number in which the
    computer should play its next tile. """
    
    count = 0
    for i in range(len(List) - 1):
        if (List[i] == 'P' and List[i+1] == 'P') or \
        (List[i] == 'C' and List[i+1] == 'C'):
             count += 1
        else:
            count = 0
        if count >= 2:
            
            # If the computer has a 3-in-a-row, returns the column number the computer
            # should play its next tile in to complete the 4-in-a-row
            if List[i] == 'C':
                if i+2 < len(List) and List[i+2] == 0:
                        return i + 2
                elif i - 2 >= 0 and List[i-2] == 0:
                    return i - 2
                
            # If the player has 3-in-a-row, returns the column number the computer should
            # play its next tile in to block the player from creating a 4-in-a-row
            elif List[i] == 'P':
                if i+2 < len(List) and List[i+2] == 0:
                    return i + 2
                elif i - 2 >= 0 and List[i-2] == 0:
                    return i - 2
    
    # if no three in a row is found or there are no openings on either side of a 
    # 3-in-a-row, "nothing" is returned
    return "nothing"
        
    
class Player:
    """ The human player is stored as an object in the class Player. A method is 
    provided to add a tile to the board when it is their turn. """
    
    def __init__(self):
        self.name = 'player'
        self.color = ''
        
    def TileColor(self):
        self.color = chooseColor()
    
    def addTile(self, window, buttonList, boardList):
        """ This method manages the player's turn: it takes input from the getMouse function
        to place a tile in a particular column. This tile is drawn on the graphics screen.
        It also updates the boardList data set and the button count of the button that was
        pressed. """
        waiting = True
        # Waiting is set to false once a button is clicked. This prevents the user's
        # turn from ending after clicking somewhere on the screen other than on an
        # active button.
        while waiting == True:
            p = window.getMouse()
            for button in buttonList:
                if button.clicked(p):
                    circ = Circle(Point(button.getX(), 300 - button.count*40), 15)
                    circ.setFill(self.color)
                    circ.draw(window)

                    button.updateCount()
                    boardList.addItem(button.count - 1, buttonList.index(button), 'P')
                    waiting = False

                    return
                

class Computer:
    """ The computer player is stored as an object in the class Computer. A method is
    provided to add a tile to the board when it is the computer's turn. """
    
    def __init__(self):
        self.name = 'computer'
        
    def addTile(self, window, buttonList, boardList):
        """ This method manages the computer's turn: it checks whether there are any 
        3-in-a-rows it should complete or block. If not, it generates a random number 
        to place a tile in the corresponding column. The tile is drawn on the graphics 
        screen. The method also updates the boardList data set and the button count of 
        the button that was pressed. """
        
        # generates a random button to press
        button = buttonList[randint(0, 5)]
    
        for i in range(len(boardList.rows)):
            
            # if there is a vertical 3-in-a-row to block or complete, the 
            # corresponding button number is chosen, and the computer no 
            # longer places a button randomly
            if find3(boardList.cols[i]) != "nothing":
                button = buttonList[i]
                
            # if there is a horizontal 3-in-a-row to block or complete
            # the corresponding button number is chosen. and the computer no 
            # longer places a button randomly
            elif find3(boardList.rows[i]) != "nothing":
                button = buttonList[find3(boardList.rows[i])]
                
            
        # checks if the choses button corresponds to a column that is already filled. If so,
        # then a different button is randomly chosen
        while button.active == False:
            button = buttonList[randint(0,5)]
        circ = Circle(Point(button.getX(), 300 - button.count*40), 15)
        circ.setFill('black')
        circ.draw(window)
        button.updateCount()
        boardList.addItem(button.count - 1, buttonList.index(button), 'C')
               
            
class Lists:
    """A list is a dataset that stores the location of the tile pieces on the board. 
    The data is stored as the instance variables rows, columns, and diagonals. Methods
    are built in to transfer the row data into columns and diagonals. In this section,
    the datasets are also checked for 4-in-a-rows."""
    
    def __init__(self):
        self.rows = [[0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
        self.cols = [[0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0], 
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]
        self.diags = [[0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0]]
        
        self.outcome = 'None yet'
        
    def addItem(self, row, col, user):
        """This method updates the data set when a tile is added to the board"""
        self.rows[row][col] = user
        
    def find4s(self):
        """ This method calls on the find4 function to determine if there is a 4-in-a-row
        of 'C's or 'P's in list of rows, list of columns, and list of diagonals. When a 
        list is checked, the find4s returns True if there are no 4-in-a-rows and returns 
        false as soon as there is a 4-in-a-row. If there is a 4-in-a-row, the outcome 
        instance variable is also updated to be either 'P' or 'C'."""
        
        # Checks the rows and columns
        for k in range(len(self.rows)):
            if find4(self.rows[k]) == 'P' or find4(self.cols[k]) == 'P':
                self.outcome = 'P'
                return False
            elif find4(self.rows[k]) == 'C' or find4(self.cols[k]) == 'C':
                self.outcome = 'C'
                return False
        
        # Checks the diagonals
        for z in range(len(self.diags)):
            if find4(self.diags[z]) == 'P':
                self.outcome = 'P'
                return False
            elif find4(self.diags[z]) == 'C':
                self.outcome = 'C'
                return False
        
        # True is returned if no 4-in-a-row's have been found. 
        return True

    def updateCols(self):
        """ When called, this method uses the rows instance variable to update the
        cols instance variable. """
        
        for i in range(6):
            for j in range(6):
                self.cols[i][j] = self.rows[j][i]
                
    def updateDiags(self, L):
        """ When called, this method uses the rows instance variable (as the parameter 'L') 
        to update the diags instance variable, which is a list of all the diagonals that are 
        at least 4 spaces long. """
        
        D1 = [L[3][0], L[2][1], L[1][2], L[0][3]]
        D2 = [L[4][0], L[3][1], L[2][2], L[1][3], L[0][4]]
        D3 = [L[5][0], L[4][1], L[3][2], L[2][3], L[1][4], L[0][5]]
        D4 = [L[5][1], L[4][2], L[3][3], L[2][4], L[1][5]]
        D5 = [L[5][2], L[4][3], L[3][4], L[2][5]]
        
        D6 = [L[2][0], L[3][1], L[4][2], L[5][3]]
        D7 = [L[1][0], L[2][1], L[3][2], L[4][3], L[5][4]]
        D8 = [L[0][0], L[1][1], L[2][2], L[3][3], L[4][4], L[5][5]]
        D9 = [L[0][1], L[1][2], L[2][3], L[3][4], L[4][5]]
        D10 = [L[0][2], L[1][3], L[2][4], L[3][5]]
        
        Diagonals = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10]    
        
        self.diags = Diagonals
        
        
def displayResult(window, outcome):
    """ When this function is called, it uses the parameter 'outcome' to print who
    has won in the graphics window. """
    
    # prints a message when the human player wins
    if outcome == 'P':
        text = Text(Point(172, 385), 'You Win!!!')
        text.setSize(30)
        text.draw(window)
        
    # prints a message when the computer wins
    elif outcome == 'C':
        text = Text(Point(172, 385), "You Lose :'( ")
        text.setSize(30)
        text.draw(window)
        
    # prints a message when the game is a tie
    elif outcome == 'Tie':
        text = Text(Point(172, 385), "It's a Tie")
        text.setSize(30)
        text.draw(window)
    
    
def game(Board, Player1, Player2, Buttons, window):
    """ This function executes the bulk of the game. It controls when it is each
    player's turn and it calls on displayResult to print who has won at the 
    appropriate time. """
    
    count = 0
    # The count is increased each time a new tile is added to the board.
    # The while loop prevents more tiles from being added when all 36 spots 
    # have been played in or when a 4-in-a-row has been found. 
    while count < 36 and Board.find4s() == True:
        
        # To ensure that the players take turns, the count value determines whose turn it is.
        if count % 2 == 0:
            Player1.addTile(window, Buttons, Board)
            Board.updateCols()
            Board.updateDiags(Board.rows)
            Board.find4s()
            count += 1
    
        else:
            Player2.addTile(window, Buttons, Board)
            Board.updateCols()
            Board.updateDiags(Board.rows)
            Board.find4s()
            count +=1
    
    # If the count reaches 36 and there is no winner, the game outcome is set to be a tie.
    if count == 36:
        Board.outcome = 'Tie'
    
    # Once the game is over, the buttons are deactivated so that no more tiles can be added.
    for button in Buttons:
        button.deactivate()
        
    displayResult(window, Board.outcome)
    
    return
  
    
def main():
    """ Main generates and sets up the graphics window in which the game will
    be played. It also creates 'boardList', which is the list representation of the board. 
    The human and computer players are created, and then the game function is called to 
    initiate game play. """
    
    window = GraphWin("Connect 4", 345, 425)
    buttonList = drawButtons(window)
    addBoard(window)
    boardList = Lists()
    Human = Player()
    Human.TileColor()
    Comp = Computer()
    
    game(boardList, Human, Comp, buttonList, window)
    
    raw_input("press enter to quit")
        
    
main()
