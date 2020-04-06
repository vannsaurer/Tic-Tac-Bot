import cv2
import random
#XOPositions = []
gameBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
playerTurn = None




def checkWin():
    # check down columns
    token = "O" if playerTurn2 else "X"
    output = False

    # Horizontal and Vertical lines
    for row in range(3):
        hCount = 0
        vCount = 0
        for col in range(3):
            if (gameBoard[row][col] is token):
                hCount += 1
            if (gameBoard[col][row] is token):
                vCount += 1
        if hCount == 3 or vCount == 3:
            output = True

    # Diagonal lines
    if (gameBoard[0][0] is token and gameBoard[1][1] is token and gameBoard[2][2] is token):
        output = True
    elif (gameBoard[2][0] is token and gameBoard[1][1] is token and gameBoard[0][2] is token):
        output = True

    if output:
        name = "player " if playerTurn else "CPU "
        print("The " + name + "is the winner!\n")

    gameWon = output




def tryMove( row, col):
    '''
    Try to make a move, returns true if successful
    returns false if row or column are not in range, or if position occupied
    '''

    if playerTurn2 : token = "O"
    else:
        token = "X"
        #cv2.putText(boardImg, strXY, (x, y), font, 5, (0, 0, 0), 2)  # For drawing the X
    if (row not in [0, 1, 2] or col not in [0, 1, 2]):
        print("\t Incorrect values")
        return False
    elif (gameBoard[row][col] == " "):
        print("Successful move (" + str(row) + ", " + str(col) + ")")
        gameBoard[row][col] = token
        return True
    else:
        print("\t Position occupied")

    return False

def AIMove():
    # Create a list of possible moves
    possibleMoves = []
    for row in range(3):
        for col in range(3):
            if gameBoard[row][col] == " ":
                possibleMoves.append((row, col))

    random.shuffle(possibleMoves)
    print(possibleMoves)
    return possibleMoves[0]


def click_event(event, x, y, flags, param):
    global playerTurn2

   # cv2.imshow('image', boardImg)
    if event == cv2.EVENT_LBUTTONDOWN:
        playerTurn2 = True

       # XOPositions.append((x, y))

        #print(XOPositions)
       # print(x, ', ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x) + ', '+ str(y)
        strXY = "X"
        cv2.circle(boardImg, (x, y), 40, (0, 0, 0), 2)  # For drawing the O
        # cv2.putText(boardImg, strXY, (x, y), font, 5, (0, 0, 0), 2)#For drawing the X


        state = "O"
        r=0
        c=0
        if (x < 300) & (y < 300):
            #gameBoard[0][0] = state
            r=0
            c=0
        elif (x > 300) & (x < 500) & (y < 300):
            #gameBoard[0][1] = state
            r = 0
            c = 1
        elif (x > 500) & (y < 300):
            #gameBoard[0][2] = state
            r = 0
            c = 2
        elif (x < 300) & (y > 300) & (y < 500):
            #gameBoard[1][0] = state
            r = 1
            c = 0
        elif (x > 300) & (x < 500) & (y > 300) & (y < 500):
            #gameBoard[1][1] = state
            r = 1
            c = 1
        elif (x > 500) & (y > 300) & (y < 500):
            #gameBoard[1][2] = state
            r = 1
            c = 2
        elif (x < 300) & (y > 500):
            #gameBoard[2][0] = state
            r = 2
            c = 0
        elif (x > 300) & (x < 500) & (y > 500):
            #gameBoard[2][1] = state
            r = 2
            c = 1
        elif (x > 500) & (y > 500):
            #gameBoard[2][2] = state
            r = 2
            c = 2
        successfulMove = tryMove(r,c)
        playerTurn2 = False


        print("Ai's Turn\n")
        move = AIMove()
        print(move)
        print(move[0])
        successfullMove = tryMove(move[0], move[1])
        if (move[0] == 0) & (move[1] == 0):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (100, 150), font, 5, (0, 0, 0), 2)#For drawing the X
        elif (move[0] == 0) & (move[1] == 1):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (400, 150), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 0) & (move[1] == 2):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (600, 150), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 1) & (move[1] ==0):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (100, 450), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 1) & (move[1] ==1):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (400, 450), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif(move[0] == 1) & (move[1] ==2):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (600, 450), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 2) & (move[1] ==0):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (100, 650), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 2) & (move[1] ==1):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (400, 650), font, 5, (0, 0, 0), 2)  # For drawing the X
        elif (move[0] == 2) & (move[1] ==2):
            font = cv2.FONT_HERSHEY_SIMPLEX
            strXY = "X"
            cv2.putText(boardImg, strXY, (600, 650), font, 5, (0, 0, 0), 2)  # For drawing the X

        print(gameBoard)
        return successfulMove

boardImg = cv2.imread('ticTacToeBoard.png')
#cv2.imshow('image', boardImg)
#calling the click_event function on the image



# load the image, clone it, and setup the mouse callback function


# keep looping until the 'q' key is pressed
while True:
    cv2.setMouseCallback('image', click_event)
    # display the image and wait for a keypress
    cv2.imshow("image", boardImg)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, break from the loop and Quit Game
    #Game quits if there is a win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if key == ord("q"):
        break

    #if checkWin():
     #   break


cv2.destroyAllWindows()