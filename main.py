import function
import sys

name1=""
name2=""
player=0
player2=0

print("The goal of this game is to reach 100. \nFor every roll you get the point seen on the dice itself, but, if you roll 1 you'll lose the point. To save the point you have to bank the point by pass the turn \nLet's get started!! \n")
start=input("Start the game? y/n ")
if start=="n":
  print("closing the game...")
  sys.exit()


name1 = input("What's your name?\n")
name2 = input("Wanna play with another PLAYER or against CPU? Insert another name or CPU\n")
function.cls(name1,player,name2,player2)


while True:
  temp = 0 
  x=""
  y=""
  print(f'It\'s {name1} turn \n')
  player=function.roll(player)
  function.cls(name1,player,name2,player2)
  if player>=100:
    print(f'{name1} Win!')
    y=input("Wanna play again? y/n ")
    if y == "n":
      break
    else:
      player2=0
      player=0
      function.cls(name1,name2)
      continue
  if name2 != "CPU":    
    print(f'It\'s {name2} Turn \n')
    player2=function.roll(player2)
    function.cls(name1,player,name2,player2)
    if player2 >=100:
      print(f'{name2} WIN!')
      y=input("Wanna play again? y/n ")
      if y == "n":
        print("Exiting...")
        break
      else:
        player2=0
        player=0
        function.cls(name1,player,name2,player2)
        continue
  else:  
    print("It's CPU turn \n")
    player2=function.CPU(player,player2)
    function.cls(name1,player,name2,player2)
    if player2 >=100:
      print("GAME OVER, CPU win!")
      y=input("Wanna play again? y/n ")
      if y == "n":
        print("Exiting...")
        break
      else:
        player=0
        player2=0
        function.cls(name1,player,name2,player2)
        continue
    
      
    
