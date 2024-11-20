import random
import os
import time


def cls(name1,player,name2,player2):
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'{name1} has {player} points and {name2} has {player2} points \n')
    time.sleep(1)

def roll(player):
  temp=0
  x=""
  while True:
    roll = random.randint(1,6)
    print(f'You rolled {roll} \n')
    if roll==1:
      print(f'Pigged out!...')
      temp=0
      time.sleep(2)
      return player
    else:
      temp=temp+roll
      if check_win(player,temp):
        player=player+temp
        return player
      x = input(f'You have {temp} point awaited to bank, Another roll? y/n ')
      if x == "y":
        continue
      else:
        player=player+temp
        return player

def CPU(player, player2):
  temp=0
  while True:
    roll = random.randint(1,6)
    if roll==1:
      print(f'CPU has been pigged out!...')
      time.sleep(2)
      temp=0
      return player2
    else:
      temp=temp+roll
      if check_win(player2,temp):
        player2=player2+temp
        return player2
      if player2>player:
        if temp < 15:
          continue
        else:
          player2=player2+temp
          print(f'CPU made {temp} points')
          time.sleep(2)
          return player2
      else:
        if temp < 20:
          continue
        else:
          player2=player2+temp
          print(f'CPU made {temp} points')
          time.sleep(2)
          return player2

def check_win(player,temp):
  if player + temp >= 100:
    return True
    
    
  
