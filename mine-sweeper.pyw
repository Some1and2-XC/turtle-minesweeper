import turtle, random, time, math
#-----------------------functions--------------------
def drawGrid():
    global squaresFlagged, flag, partsDrawn
    if flag is True:
        clr = "red"
    else:
        clr = "white"

    myWin.bgcolor(clr)

    for row in range(0,len(coordinates),1):
        for column in range(0,len(coordinates[row]),1):
            if [row, column] not in partsDrawn:
                gridSquare.goto(coordinates[row][column])

                if map[row][column] <= 1:
                    gridSquare.color('grey')
                    gridSquare.pencolor('grey')
                    gridSquare.stamp()



                # else:4
                #     gridSquare.color("white")
                #     gridSquare.pencolor("white")
                #     gridSquare.stamp()

    for i in range(0, len(squaresFlagged)):
        gridSquare.goto(coordinates[squaresFlagged[i][1]][squaresFlagged[i][0]])
        gridSquare.color("red")
        gridSquare.pencolor("red")
        gridSquare.stamp()

    # for row in range(0,len(coordinates),1):
    #     for column in range(0,len(coordinates[row]),1):
    #         # if [row, column] not in partsDrawn:
    #         if map[row][column] > 2:
    #             pen.goto(coordinates[row][column])
    #             pen.goto(pen.xcor() - 2, pen.ycor() - 5)
    #
    #             pen.write(str(map[row][column] - 2))
    #                 # partsDrawn.append([row,column])



    myWin.update()
    return

def leave():
    myWin.bye()
    return

def newBoard():
    global gridDimension, map, amntOfBombs
    map = []
    for i in range(0, gridDimension):
        map.append([])
        for j in range(0, gridDimension):
            map[i].append(0)


    for i in range(0, amntOfBombs):
        x = "z"
        while x == "z":
            x = random.randint(0, gridDimension - 1)
            y = random.randint(0, gridDimension - 1)
            if map[x][y] == 0:
                map[x][y] = 1
            else:
                x = "z"


    return

def pieceClick(x, y):
    global usableSpace, gutterOffset, gridSquareSize, searchedPieces, gridDimension, flag, squaresFlagged, win
    x = int(((+ int(-1 * usableSpace / 2) + gutterOffset - x) / -gridSquareSize) + 0.5)
    y = int(((int(usableSpace / 2) - gutterOffset - y) / gridSquareSize) + 0.5)
    searchedPieces = []
    if flag is False:
        if 0 <= x < gridDimension and 0 <= y < gridDimension:
            if [x, y] not in squaresFlagged:
                uncover(x, y)
    else:
        if 0 <= x < gridDimension and 0 <= y < gridDimension:
            if map[y][x] <= 1:
                hasFlag = False
                for i in range(0, len(squaresFlagged)):
                    if squaresFlagged[i][0] == x and squaresFlagged[i][1] == y:


                        del squaresFlagged[i]
                        hasFlag = True
                        break
                if hasFlag is False:
                    gridSquare.goto(coordinates[y][x])
                    gridSquare.color("red")
                    gridSquare.pencolor("red")
                    gridSquare.stamp()
                    squaresFlagged.append([x, y])
                else:
                    gridSquare.goto(coordinates[y][x])
                    gridSquare.color("grey")
                    gridSquare.pencolor("grey")
                    gridSquare.stamp()
                myWin.update()
    winCheck()
    if win == True:
        pen.goto(0, 0)
        pen.write("You Win!", align=("center"), font=("arial", 25, "bold"))
        myWin.exitonclick()



    return

def uncover(j, i):
    global map, gridDimension, searchedPieces, playing, squaresFlagged, firstClick


    searchedPieces.append([j, i])
    
    if firstClick is True and map[i][j] == 1:
            while map[i][j] == 1:
                newBoard()
                
    if map[i][j] == 0:
        pieceNo = 0
        for k in range(0, 3):
            for l in range(0, 3):
                if 0 <= i + k - 1 < gridDimension and 0 <= j + l - 1 < gridDimension:
                    if map[i + k - 1][j + l - 1] == 1:
                        pieceNo += 1
        map[i][j] = 2 + pieceNo
        gridSquare.goto(coordinates[i][j])
        gridSquare.color("white")
        gridSquare.stamp()
        if pieceNo == 0:

            k = 0

            while k <= len(squaresFlagged) - 1:
                if squaresFlagged[k][0] == j and squaresFlagged[k][1] == i:
                    del squaresFlagged[k]
                k += 1

            for k in range(0, 3):
                for l in range(0, 3):
                    doUncover = True
                    for m in range(0, len(searchedPieces)):
                        if searchedPieces[m] == [int(j + l - 1), int(i + k - 1)]:
                            doUncover = False
                    if 0 > i + k - 1 or i + k - 1 >= gridDimension or 0 > j + l - 1 or j + l - 1 >= gridDimension:
                        doUncover = False
                    if doUncover is True:
                        uncover(j + l - 1, i + k - 1)
                        
            return
        else:

            pen.goto(coordinates[i][j])
            pen.goto(pen.xcor() - 2, pen.ycor() - 5)
            pen.write(str(map[i][j] - 2))
    
    if map[i][j] == 1:
        gridSquare.goto(coordinates[i][j])
        gridSquare.color("blue")
        gridSquare.stamp()
        myWin.update()
        myWin.exitonclick()
        
    firstClick = False
    return

def flagToggle():
    global flag
    if flag is False:
        myWin.bgcolor("red")
        flag = True
    else:
        myWin.bgcolor("white")
        flag = False
    return

def winCheck():
    global map, squaresFlagged, amntOfBombs, win

    flagWin = False
    print(amntOfBombs, len(squaresFlagged))
    if len(squaresFlagged) == amntOfBombs:
        flagWin = True
        for i in range(0, len(squaresFlagged)):
            if map[squaresFlagged[i][1]][squaresFlagged[i][0]] != 1:
                flagWin = False
                break

    pieceWin = True
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 0:
                pieceWin = False
    if pieceWin is True or flagWin is True:
        win = True


    return

#---------------importing map from external file--------------------
map = []
useImport = False

firstClick = True

win = False


if useImport is True:
    mapFile = open('map.txt','r')

    for line in mapFile:
        temp = line.strip('\n')
        temp = list(temp)
        map.append(temp)
    mapFile.close()
#that was a list of list of strings...
#convert each to an integer
for i in range(0,len(map),1):
    for j in range(0,len(map[i]),1):
        map[i][j] = int(map[i][j])


#---------------turtle and grid definitions--------------------
#we will be using a 600x600 screen no matter what
#with a 10 pixel buffer near the edge
myWin = turtle.Screen()
myWin.setup(600,600)
myWin.tracer(0, 0)
#so the width and height both 580 pix of usable space
#and this space will be subdivided based on these 3 parameters
#gridSquareSize = 20 #each square is 20x20 pixels ---------------------
gridSquareSize = 20 #each square is 20x20 pixels ---------------------
gutterOffset = 8 #-----------give a little space on the edges
usableSpace = 580 #---------------actual usable space - leave a little on the edge
# the percentage of the board that is bombs
amntOfBombs = 12.5
gridDimension = int(usableSpace/gridSquareSize)
amntOfBombs = int((amntOfBombs / 100) * gridDimension ** 2)
playing = True
squaresFlagged = []
partsDrawn = []

flag = False

#-----now make the turtle that will draw the grid...
gridSquare = turtle.Turtle()
gridSquare.speed(0)
gridSquare.penup()
gridSquare.shape('square')
gridSquare.turtlesize(gridSquareSize/20,gridSquareSize/20)
gridSquare.color('white')
gridSquare.pencolor('black')

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)
#----now create the coordinates of each location to visit, store this in a list
#----of lists
coordinates = []
for row in range(0,gridDimension,1): #row = y, there will be gridDimension rows
    tempList = []
    for column in range(0,gridDimension,1): #column = x, there will be gridDimension columns
        x = gridSquareSize*column + int(-1*usableSpace/2) + gutterOffset
        y = int(usableSpace/2) - gridSquareSize*row - gutterOffset
        tempList.append((x,y))
    coordinates.append(tempList)

myWin.listen()
myWin.onkeypress(flagToggle, "space")

myWin.onclick(pieceClick)



myWin.update()

newBoard()
drawGrid()
#----------------do you need a game loop for autonomous movement??
#----------------it would go here
while playing is True:
    myWin.mainloop()
myWin.exitonclick()
