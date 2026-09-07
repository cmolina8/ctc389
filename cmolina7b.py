#Ceiry Molina 
#Lab 7 Extra Credit Part 2

def game():
    x = 17 
    y = int(input("Guess my number:"))
    r = x - y 

    while abs(y-x) <=2 and x != y:
        y = int(input("Close, try again:"))
        r = x-y 

    if y == x: 
        print("Good Job!!! You guessed my number!!!")

    else:
        if (y > x):
            print ("Sorry you lost. Your guess was higher than my number which was 17.")
    
        else:
            print("Sorry you lost. Your guess was lower than my number which was 17.")

ans = input ("Do you want to play my guessing game?")
while (ans == "yes"):
    game()
    ans = input("Do you want to play my guessing game?")

