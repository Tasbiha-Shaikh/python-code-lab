import random

'''
1 for snake 
-1 for water 
0 for gun
'''

computer = random.choice([-1,1,0]) 
youstr = input("enter your choice (s/w/g):")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake",-1:"water",0:"gun"}

you = youDict[youstr]

# by now you have 2 numbers , you and computer

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw")

else:
    if (computer - you) == -1 or (computer - you) == 2:     
        print("you lose")
    else:
        print("you win")


# deatil logic code 


    # if computer == -1 and you == 1:  # -1-1 = -2
    #     print("You win")

    # elif computer == -1 and you == 0:  # -1
    #     print("You lose")

    # elif computer == 1 and you == -1: # 2
    #     print("You lose")

    # elif computer == 1 and you == 0: # 1
    #     print("You win")

    # elif computer == 0 and you == -1: # 1
    #     print("You win")

    # elif computer == 0 and you == 1: # -1
    #     print("You lose")

    # else:
    #     print("Something went wrong")
