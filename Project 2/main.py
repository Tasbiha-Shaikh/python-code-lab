import random
n = random.randint(1,100)
a = -1
guesses = 1
while( a!= n):
    a = int(input("guess the number:"))
    if( a>n ):
        print("please lower number")
        guesses += 1
    elif(a<n):
        print("please higher number") 
        guesses += 1

print(f"you have guseed the number {n} correctly {guesses} attempt")

