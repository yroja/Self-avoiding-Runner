import pygame
import random
import time


width = 1000
height = 500

pygame.init()
screen = pygame.display.set_mode([width, height])


class Cell:
    def __init__(self, x, y) -> None:
        self.xcoord = x
        self.ycoord = y
        self.taken = False

    def isTaken(self) -> bool:
        return self.taken

    def draw(self):
        pygame.draw.circle(screen, (0,255,0), (self.xcoord, self.ycoord), 10, width=0)
        pygame.display.update()

    def drawFirst(self):
        pygame.draw.circle(screen, (255,0,0), (self.xcoord, self.ycoord), 10, width=0)
        pygame.display.update()

    def setTaken(self, taken:bool):
        self.taken = taken

    def getXcoord(self):
        return self.xcoord

    def getYcoord(self):
        return self.ycoord

    def connect(self, otherCell):
        pygame.draw.line(screen, (0, 255, 0), (self.xcoord, self.ycoord), (otherCell.getXcoord(), otherCell.getYcoord()), width=1)
        pygame.display.update()
        

class Grid:
    def __init__(self) -> None:
        x = 10
        y = 10
        self.grid = []
        for i in range(0, 20):
            self.grid.append([])
            for j in range(0,40):
                self.grid[i].append(Cell(x, y))
                x += 10 * 2 + 5
            x = 10
            y += 10 * 2 + 5
    
    def getGrid(self):
        return self.grid

    def check(self):
        count = 0
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[i])):
                count += 1

        print(count)

class Game:
    def __init__(self) -> None:
        self.grid = Grid().getGrid()
        self.row = int(len(self.grid) / 2)
        self.column = int(len(self.grid[0]) / 2)
        self.grid[self.row][self.column].drawFirst()
        self.grid[self.row][self.column].setTaken(True)
        self.canMove = True

    def run(self):
        while(self.canMove):
            self.move()
            pygame.display.update()
            time.sleep(0.1)

        print("GAME OVER\npress 'a' to start a new walk")
        


    def hasOptions(self, row, column) -> list:
        options = []
        if(row >= 0 and row < len(self.grid) and column >= 0 and column < len(self.grid[0])):
            if(column != len(self.grid[0]) - 1 and not self.grid[row][column + 1].isTaken()):
                options.append([row, column + 1])
            if(column != 0 and not self.grid[row][column - 1].isTaken()):
                options.append([row, column - 1])
            if(row != len(self.grid) - 1 and not self.grid[row + 1][column].isTaken()):
                options.append([row + 1, column])
            if(row != 0 and not self.grid[row - 1][column].isTaken()):
                options.append([row - 1, column])

        return options

    def move(self):
        
        options = self.hasOptions(self.row, self.column)
        if(len(options) > 0):
            choice = random.choice(options)
            self.grid[choice[0]][choice[1]].draw()
            self.grid[choice[0]][choice[1]].setTaken(True)
            self.grid[self.row][self.column].connect(self.grid[choice[0]][choice[1]])
            self.row = choice[0]
            self.column = choice[1]
        else:
            print('no possible direction to move!')
            self.canMove = False


        





if __name__ == '__main__':

    screen.fill('black')
    #initGrid()
    game = Game()
    game.run()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.fill('black')
            game = Game()
            game.run()

        

        pygame.display.update()


