#MSP
import turtle
from random import randint
from time import sleep

#initialise empty 3 by 3 grid
grid = []
grid.append([8,0,0])
grid.append([0,0,7])
grid.append([0,9,0])

SUM=15 #Each Row, Column and Diagonal will add up to 15

myPen = turtle.Turtle()
myPen._tracer(0)
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x=-150
topLeft_y=150

def text(message,x,y,size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x,y)
    myPen.write(message,align="left",font=FONT)

#A procedure to draw the grid on screen using Python Turtle
def drawGrid(grid):
  intDim=100
  for row in range(0,4):
    myPen.penup()
    myPen.goto(topLeft_x,topLeft_y-row*intDim)
    myPen.pendown()
    myPen.goto(topLeft_x+3*intDim,topLeft_y-row*intDim)
  for col in range(0,4):
    myPen.penup()
    myPen.goto(topLeft_x+col*intDim,topLeft_y)
    myPen.pendown()
    myPen.goto(topLeft_x+col*intDim,topLeft_y-3*intDim)

  for row in range (0,3):
      for col in range (0,3):
        if grid[row][col]!=0:
          text(grid[row][col],topLeft_x+col*intDim+25,topLeft_y-row*intDim-intDim+25,50)


#A function to check if the grid is a magic square
def checkGrid(grid):
  global SUM
  for row in range(0,3):
      for col in range(0,3):
        if grid[row][col]==0:
          return False
  for row in range(0,3):
    if (grid[row][0]+grid[row][1]+grid[row][2])!=SUM:
      return False
  for col in range(0,3):
    if (grid[0][col]+grid[1][col]+grid[2][col])!=SUM:
     return False
  if (grid[0][0]+grid[1][1]+grid[2][2])!=SUM:
   return False
  if (grid[0][2]+grid[1][1]+grid[2][0])!=SUM:
   return False

  #We have a magic square!
  return True

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
  #Find next empty cell
  for i in range(0,9):
    row=i//3
    col=i%3
    if grid[row][col]==0:
      for value in range (1,10):
        #Can only use numbers that have not been used yet
        if not(value in grid[0] or value in grid[1] or value in grid[2]):
          grid[row][col]=value
          #sleep(0.0001)
          myPen.clear()
          drawGrid(grid)
          myPen.getscreen().update()
          if checkGrid(grid):
            print("Grid Complete and Checked")
            return True
          else:
            if solveGrid(grid):
              return True
      break
  print("Backtrack")
  grid[row][col]=0


drawGrid(grid)
myPen.getscreen().update()
sleep(1)

solved = solveGrid(grid)
if solved:
  print("Magic Square Solved")
  text("Magic Square Solved",-130,-180,20)
else:
  print("Cannot Solve Magic Square")
  text("Cannot Solve Magic Square",-150,-180,20)

myPen.getscreen().update()
