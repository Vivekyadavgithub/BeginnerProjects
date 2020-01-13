import numpy as np
import random
ROW=10
COLUMN=10
def myboard():
  board=np.zeros((ROW,COLUMN))
  return board

r=[0,1,2,3,4,5,6,7,8,9]
c=[0,1,2,3,4,5,6,7,8,9]



def location(board,gotti,dicevalue):
          board[r][c]=gotti
          if dicevalue <11:
             return board[0][dicevalue-1] == gotti
          elif dicevalue < 21:
              return board[1][dicevalue-11] == gotti
          elif dicevalue < 31:
              return board[2][dicevalue - 21] == gotti
          elif dicevalue < 41:
              return board[3][dicevalue - 31] == gotti
          elif dicevalue < 51:
              return board[4][dicevalue - 41] == gotti
          elif dicevalue < 61:
              return board[5][dicevalue - 51] == gotti
          elif dicevalue < 71:
              return board[6][dicevalue - 61] == gotti
          elif dicevalue < 81:
            return board[7][dicevalue - 71] == gotti
          elif dicevalue < 91:
              return board[8][dicevalue - 81] == gotti
          elif dicevalue <=100:
             return board[9][dicevalue - 91] == gotti


def location2(board, gotti, dicevalue2):
  board[r][c]=gotti
  if dicevalue2 < 11:
     return board[0][dicevalue2-1] == gotti
  elif dicevalue < 21:
    return board[1][dicevalue2 - 11] == gotti
  elif dicevalue < 31:
    return board[2][dicevalue2 - 21] == gotti
  elif dicevalue < 41:
    return board[3][dicevalue2 - 31] == gotti
  elif dicevalue < 51:
    return board[4][dicevalue2 - 41] == gotti
  elif dicevalue < 61:
    return board[5][dicevalue2 - 51] == gotti
  elif dicevalue < 71:
    return board[6][dicevalue2 - 61] == gotti
  elif dicevalue < 81:
    return board[7][dicevalue2 - 71] == gotti
  elif dicevalue < 91:
    return board[8][dicevalue2 - 81] == gotti
  elif dicevalue <= 100:
    return board[9][dicevalue2 - 91] == gotti

def flip(board):
    print(np.flip(board, 0))

def end(dicevalue,dicevalue2):
  if dicevalue == 100:
    print("player 1 won")
    gameover=True
  elif dicevalue2 == 100:
    print("player 2 won")
    gameover=True


gameover=False
board=myboard()
print(board)
turn=0
dicevalue=1
dicevalue2=1
while not gameover:
  if turn ==0:
    print(input("player1 chance"))
    col=int(random.randint(1,6))
    print(col)
    dicevalue += col
    print(dicevalue)
    location(board,1,dicevalue)
    turn+=1

  elif turn ==1:
    print(input("player 2 chance"))
    col=int(random.randint(1,6))
    print (col)
    dicevalue2 += col
    print(dicevalue2)
    location2(board, 2, dicevalue2)

    turn-=1
  flip(board)