import random

def game():
    print("you are playing the game")
    score = random.randint(1,60)

    #fetch the score
    with open("hiscore.txt","r") as f:
        hiscore= f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score {score}")
    print(f"Old high score: {hiscore}")
    if(score>hiscore):
        # write this hiscore in this file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
            print("High score updated!")
    else:
        print(" Score not higher, file not updated")
    
    return score

game()


# import random

# def game():
#     print("You are playing the game")
#     score = random.randint(1, 60)

#     # Read previous hiscore
#     try:
#         with open("hiscore.txt", "r") as f:
#             content = f.read()
#             hiscore = int(content) if content.strip() != "" else 0
#     except FileNotFoundError:
#         hiscore = 0

#     print(f"Your score: {score}")
#     print(f"Old high score: {hiscore}")

#     # Update only if score is higher
#     if score > hiscore:
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
#         print("✅ High score updated!")
#     else:
#         print("❌ Score not higher, file not updated")

# game()
