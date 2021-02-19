import random
def quiz():
  print("\n Answer the following! ")
  num1 = int(random.randrange(0,10))
  num2 = int(random.randrange(0,10))
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
    quiz()
quiz()