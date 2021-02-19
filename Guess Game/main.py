# Number Games
import random
#Guess funtion

def guess():
  print("\n Entered Guess Number game")
  c = int(random.random())
  print("Number generated!")
  g = input("Please guess the Number: ")
  if (g == c):
    print("Congrats! You are correct The number is", c)
    guess()
  else:
    print("You loose👎 The number was" ,c)
    guess()
  
guess()