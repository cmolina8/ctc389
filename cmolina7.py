#Ceiry Molina 
#Lab 2 Part 7

x = 17 

y = int(input("Guess my number:"))

while abs(y-x) <=2 and x != y:
    y = int(input("Close, try again:"))

if y == x: 
    print("Good Job!!! You guessed my number!!!")

else:
    if (y > x):
        print ("Sorry you lost. Your guess was higher than my number which was 17.")
    
    else:
        print("Sorry you lost. Your guess was lower than my number which was 17.")

