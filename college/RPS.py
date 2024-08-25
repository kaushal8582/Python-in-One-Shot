import random

arr =["ROCK","PAPER","SCISSORS"]

userInput = input("Enter ROCK PAPER SCISSORS : ").capitalize()

C_H = random.choice(arr).capitalize()

print(C_H,userInput)

if(userInput==C_H):
  print("Game is tie")
elif((userInput=="ROCK" and C_H=="SCISSORS") or (userInput=="PAPER" and C_H=="ROCK")  or (userInput=="SCISSORS"and C_H=="PAPER")) :
  print("You win")
else:
  print("You lose")