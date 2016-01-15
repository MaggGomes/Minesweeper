from graphics import *
from square import*
import random


class Bug(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.move = 0
        self.position = "bot"
        self.image = bug1  # Can be 1 ,2 or 3 to simulate bug movement

    def update(self):
        self.x += 0.5
        self.move += 0.5
        if self.x >= (screen_width - 100):
            self.x = 100
            if self.position == "bot":
                self.position = "top"
                self.y = 20
            elif self.position == "top":
                self.position = "bot"
                self.y = 365
        if self.move == 5:
            self.move = 0
            if self.image == bug1:
                self.image = bug2
            elif self.image == bug2:
                self.image = bug3
            elif self.image == bug3:
                self.image = bug4
            else:
                self.image = bug1
        printimg(self.image, self.x, self.y)


class Minesweeper(object):
    def __init__(self,width, height, x, y, mines):
        self.width = width
        self.height = height
        self.done = False
        self.board= [[Square(square, size_square, 0, 0) for i in range(self.height)] for j in range(self.width)]
        self.num_mines = mines
        self.mouse = MouseButtons
        self.bug = Bug(x, y)

    def squareinit(self):
        x = 75
        y = 100

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                squaretemp = Square(square, size_square, x, y)
                self.board[i][j] = squaretemp
                y = y + size_square + 2
            y = 100
            x = x + size_square + 2

    def setmines(self):
        bmines = 0
        while bmines < self.num_mines:
            row = random.randint(0, self.height-1)
            col = random.randint(0, self.width-1)

            if not self.board[col][row].is_mined:
                self.board[col][row].is_mined = True
                bmines += 1

    def squareaddcount(self, a, b):
         if 0 <= a < self.width and 0 <= b< self.height:
                if not self.board[a][b].is_mined:
                    self.board[a][b].mine_count+=1

    def setminecounter(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].is_mined:
                    self.squareaddcount(i - 1, j - 1)
                    self.squareaddcount(i - 1, j)
                    self.squareaddcount(i - 1, j + 1)
                    self.squareaddcount(i, j + 1)
                    self.squareaddcount(i + 1, j + 1)
                    self.squareaddcount(i + 1, j)
                    self.squareaddcount(i + 1, j - 1)
                    self.squareaddcount(i, j - 1)

    def startboard(self):
        self.squareinit()
        self.setmines()
        self.setminecounter()

    def boarduncover(self, a, b):
        if a < 0 or a >= self.width or b < 0 or b >= self.height or self.board[a][b].revealed or self.board[a][b].flagged:
                return

        self.board[a][b].revealed = True
        if self.board[a][b].mine_count > 0:
                return

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                self.boarduncover(a + i, b + j)

    def boardhover(self, a, b, click):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].checkcollision(a, b):
                    if click == 1:
                        if self.board[i][j].is_mined:
                            self.board[i][j].revealed = True
                            self.done = True
                        elif not self.board[i][j].revealed:
                            if not self.board[i][j].flagged:
                                self.boarduncover(i, j)

                    elif click == 3:
                        if self.board[i][j].flagged:
                            self.board[i][j].flagged = False
                        else:
                            self.board[i][j].flagged = True

    def printboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                printimg(self.board[i][j].image, self.board[i][j].x, self.board[i][j].y)

    def updateboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].revealed:
                    if self.board[i][j].is_mined:
                        self.board[i][j].image = mine
                    else:
                        if self.board[i][j].mine_count == 0:
                            self.board[i][j].image = square_pressed
                        elif self.board[i][j].mine_count == 1:
                            self.board[i][j].image = one
                        elif self.board[i][j].mine_count == 2:
                            self.board[i][j].image = two
                        elif self.board[i][j].mine_count == 3:
                            self.board[i][j].image = three
                        elif self.board[i][j].mine_count == 4:
                            self.board[i][j].image = four
                        elif self.board[i][j].mine_count == 5:
                            self.board[i][j].image = five
                        elif self.board[i][j].mine_count == 6:
                            self.board[i][j].image = six
                        elif self.board[i][j].mine_count == 7:
                            self.board[i][j].image = seven
                        elif self.board[i][j].mine_count == 8:
                            self.board[i][j].image = eight
                else:
                    if self.board[i][j].flagged:
                        self.board[i][j].image = flag
                    else:
                        self.board[i][j].image = square
        self.printboard()
