# Number Games
import random

#start function 

def start():
  print("\n Welcome")
  q=input('''Which game do u want to choose? \n
  GuessGame(g):
    NumQuiz(q): ''')
  
  if q=='g'or q=='G':
      guess()
  elif (q == 'q'or q=='Q'):
    quiz()
  else:
    print(''' \n Unknown command! reply with g or q''')
    start()

#Guess funtion

def guess():
  print("\n Entered Guess Number game")
  c = random.randrange(1,10)
  print("Number generated!")
  g = input("Please guess the Number: ")
  if g == c :
    print("Congrats! You are correct The number is", c)
  else:
    print("You loose👎 The number was" ,c)
    e = input("Exit(e)   Restart(r): ")
    if (e=="e" or e=="E"):
      print("\nExitting")
      start()
    elif (e=="r" or e=="R"):
      print("\n restarting")
      guess()
    else:
      print("\n Something went wrong, Exitting! ")
      start()
  
#Numquiz function
def quiz():
  print("\n Answer the following! ")
  num1 = random.randrange(0,10)
  num2 = random.randrange(0,10)
  olist = ["+","*","-","/"]
  ope = random.choice(olist)
  if(ope=='+'):
    print(num1,'+',num2,'= ')
    ans = int(input(""))
    cans = (num1 + num2)
    if(cans==ans):
      print("You are correct")
      quiz()
    else:
      print("You are wrong, the answer is", cans)
      quiz()
  elif(ope=='-'):
    print(num1,'-',num2,'= ')
    ans = int(input(""))
    cans = (num1 - num2)
    if(cans==ans):
      print("You are correct")
      quiz()
    else:
      print("You are wrong, the answer is", cans)
      quiz()
  elif(ope=='*'):
    print(num1,'*',num2,'= ')
    ans = int(input(""))
    cans = (num1 * num2)
    if(cans==ans):
      print("You are correct")
      quiz()
    else:
      print("You are wrong, the answer is", cans)
      quiz()
  elif(ope=="/"):
    print(num1,'÷',num2,'= ')
    ans = int(input(""))
    cans = (num1 / num2)
    if(cans==ans):
      print("You are correct")
      quiz()
    else:
      print("You are wrong, the answer is", cans)
      quiz()
  else:
    print("invalid commad! Exitting")
    start()
start()
