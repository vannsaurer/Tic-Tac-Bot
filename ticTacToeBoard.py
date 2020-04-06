import cv2
import random
#XOPositions = []
gameBoard = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
playerTurn = None

def click_event(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
       # XOPositions.append((x, y))

        #print(XOPositions)
       # print(x, ', ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = str(x) + ', '+ str(y)
        strXY = "X"
        cv2.circle(boardImg, (x, y), 40, (0, 0, 0), 2)  # For drawing the O
        # cv2.putText(boardImg, strXY, (x, y), font, 5, (0, 0, 0), 2)#For drawing the X
        cv2.imshow('image', boardImg)

        state = "O"
        if (x < 300) & (y < 300):
            gameBoard[0][0] = state
        elif (x > 300) & (x < 500) & (y < 300):
            gameBoard[0][1] = state
        elif (x > 500) & (y < 300):
            gameBoard[0][2] = state

        elif (x < 300) & (y > 300) & (y < 500):
            gameBoard[1][0] = state
        elif (x > 300) & (x < 500) & (y > 300) & (y < 500):
            gameBoard[1][1] = state
        elif (x > 500) & (y > 300) & (y < 500):
            gameBoard[1][2] = state

        elif (x < 300) & (y > 500):
            gameBoard[2][0] = state
        elif (x > 300) & (x < 500) & (y > 500):
            gameBoard[2][1] = state
        elif (x > 500) & (y > 500):
            gameBoard[2][2] = state

        print(gameBoard)

boardImg = cv2.imread('ticTacToeBoard.png')
cv2.imshow('image', boardImg)
#calling the click_event function on the image
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()