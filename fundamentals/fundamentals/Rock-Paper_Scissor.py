import random

arr = ["Rock", "Paper", "Scissors"]
rounds = 5
userWon = 0
compWon = 0

while rounds  and compWon != 3 and userWon != 3:
    print(rounds, compWon, userWon)
    compChoice = arr[random.randint(0, 2)]
    userChoise = input("Rock, Paper, Scissors 1, 2, 3: ")
    # print(userChoise + "  " + compChoice)
    if userChoise == "Rock" and compChoice == "Paper" or userChoise == "Scissors" and compChoice == "Rock" or userChoise == "Paper" and compChoice == "Scissors":
        print('Comp got it')
        compWon = compWon +1
    elif userChoise == "Paper" and compChoice == "Rock" or userChoise == "Rock" and compChoice == "Scissors" or userChoise == "Scissors" and compChoice == "Paper":
        print('User got it')
        userWon = userWon +1
    else:
        print(userChoise + " = " + compChoice)
    rounds = rounds - 1

if compWon > userWon:
  print("Comp won!!!")
elif compWon > userWon:
  print("=====")
else:
  print("User won!!!")
  
  


