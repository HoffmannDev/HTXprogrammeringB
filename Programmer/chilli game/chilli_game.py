chocolates = 12
print("This is The Chili Pepper Game!")
print("There are 13 chocolates and 1 chili pepper.")
print("Each of us will pick between one and three chocolates.")
print("The object of the game is to leave your opponent with only the chili pepper left to pick on the last turn.")
print("Okay here we go!")
print("I will go first, but i am not greedy so i only take 1 chocolate.")

def game():
    global chocolates
    i = int(input("Your turn!"))
    if i >= 1 and i < 4:
        g = 4 - i
        chocolates -= 4
        print("I take", g ,"chocolates and there is", chocolates , "left.")

        if chocolates > 0:
            print("Now it is your turn!")

        if chocolates == 0:
            print("I win, now you have to eat the chilli :)")

    else:
        print("Don't try to break the rules!")
        print("Try again")

while chocolates >= 1:
    game()
