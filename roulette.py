import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # i just copied this cause i thought it's gonna be distracting if that msg keeps showing up
import pygame

pygame.mixer.init()
spin_sound = pygame.mixer.Sound("roulette/roulette.mp3")
lose_sound = pygame.mixer.Sound("roulette/Womp_Womp.mp3")
win_sound = pygame.mixer.Sound("roulette/win.mp3")

balance = int(input("How much money do you want to bet?: "))
time.sleep(1)
print(f"You bet {balance}€\n")

rules  = (input("Do you want to double or tripple your money?: "))
rules = rules.lower()
if rules == 'double':

  bets = ['black', 'red', 'odd', 'even']
  bet = input("Select a bet (Red/Black/Even/Odd): ")
  bet = bet.lower()
  if bet in bets:
    print("You bet your money on "+ bet.upper())
    time.sleep(0.5)
    print("  The Roulette is spinning . . .\n")
    spin_sound.play()
    time.sleep(4)

elif rules == 'tripple':
   bets2 = ['1-12', '13-24','25-36']
   bet2 = input("Select a bet range (1-12/13-24/25-36)")
   if bet2 in bets2:
      print("you bet your money on " + bet2)
      print("  The Roulette is spinning . . .\n")
      spin_sound.play()
      time.sleep(4)
   
else:
    print("type a valid value like 'tripple' or 'double'")
    exit()


Green = [0] 
Black = [2, 4, 6 ,8 ,10 ,11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
Red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]



n = random.randint(0, 36)

spin_result = n 

if spin_result in Black:
 color = "black"
 print(""*5 ,n, 'BLACK')
elif spin_result in Red:
 color = "red"
 print(""*5 ,n, 'RED')
elif spin_result in Green:
 color = "green"
 print(""*5 ,n , 'GREEN')


if spin_result % 2 == 0:
    number_type = "even"
else:
    number_type = "odd"


if spin_result >= 1 and spin_result <= 12:
   ranges = "1-12"
elif spin_result >=13 and spin_result <= 24:
   ranges = "13-24"
elif spin_result >= 25 and spin_result <= 36:
   ranges ="25-36"

if rules == 'double':
    if bet == color:
        print(" You won",balance*2, end="€")
    elif bet == number_type:
       win_sound.play()
       print(f"You won {balance*2}€")
       time.sleep(4)

    else:
        print(f" You lost {balance}€")
        lose_sound.play()
        time.sleep(4)
elif rules == 'tripple':
    if bet2 == ranges:
       win_sound.play()
       print(f"You won {balance*3}€")
       time.sleep(4)
    else:
        print(f" You lost {balance}€")
        lose_sound.play() #this is why i made this to begin with 
        time.sleep(4)
