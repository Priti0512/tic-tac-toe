def sum(a,b,c):
    return a+b+c

def printBoard(Xstate, Zstate):
    zero = 'X' if Xstate[0] else ('0' if Zstate[0] else 0)
    One = 'X' if Xstate[1] else ('0' if Zstate[1] else 1)
    two = 'X' if Xstate[2] else ('0' if Zstate[2] else 2)
    three = 'X' if Xstate[3] else ('0' if Zstate[3] else 3)
    four = 'X' if Xstate[4] else ('0' if Zstate[4] else 4)
    five = 'X' if Xstate[5] else ('0' if Zstate[5] else 5)
    six = 'X' if Xstate[6] else ('0' if Zstate[6] else 6)
    seven = 'X' if Xstate[7] else ('0' if Zstate[7] else 7)
    eight= 'X' if Xstate[8] else ('0' if Zstate[8] else 8)
    print(f"{zero} | {One} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
    print(f"--|---|---")

def checkwin(Xstate, Zstate):
    wins  = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(Xstate[win[0]],Xstate[win[1]], Xstate[win[2]]) == 3):
            print("X's won the match")
            return 1

        if(sum(Zstate[win[0]],Zstate[win[1]], Zstate[win[2]]) == 3):
            print("0's won the match")
            return 0
        
    return -1


if __name__ == "__main__":
  Xstate = [0,0,0,0,0,0,0,0,0]
  Zstate = [0,0,0,0,0,0,0,0,0]
  turn = 1 #1 for X o for 0
  print("Welcome to Tic Tac Toe")
  while(True):
      printBoard(Xstate,Zstate)
      if (turn == 1):
          print("X's chance")
          value = int (input("Please Enter a value : "))
          Xstate[value] = 1
      else:
          print("0's chance")
          value = int(input("Please Enter a number: "))
          Zstate[value] = 1
      cwin = checkwin(Xstate, Zstate)
      if(cwin != -1):
          print("Match Over")
          break
      turn = 1-turn

