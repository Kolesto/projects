from random import randrange
from math import ceil
money = 1000 #The player begin each game with 100 $
out = False
while money != 0 and out == False:
    #Take the number on which the player want to bet and the bet
    print("You have: ", money, "$")
    number_choosed = -1
    while number_choosed < 0 or number_choosed > 49:
        number_choosed = input("Give us the number between 0 and 49 on which your wanna bet!\n")
        try:
            number_choosed = int(number_choosed)
        except ValueError:
            print("You didn't choose a number")
            number_choosed = -1
            continue
        if number_choosed < 0:
            print("You cannot choose a number smaller than 0")
        if number_choosed > 49:
            print("You cannot choose a number greater than 49")
    bet = -1
    while bet < 0 or bet > money:
        bet = input("Give us how much money you want to bet!\n")
        try:
            bet = int(bet)
        except ValueError:
            print("You didn't choose a number")
            bet = -1
            continue
        if bet <= 0:
            print("You cannot bet  0 and less")
        if bet > money:
            print("You cannot bet more than you have, you have: ", money, "$")       
    #Generate a random number between 0 and 49
    random_number = randrange(50)
    print("The number that have occured is: ", random_number)
    #Compare if the number generated is the same as the one choosed
    odd_random_number = random_number%2
    odd_number_choosed = number_choosed%2
    if random_number == number_choosed:
        money += ceil(bet*3)
        print("You won, you receive: ", ceil(bet*2), "$")
    #Compare if the number generated and choosed are both even or odd
    elif random_number % 2 == number_choosed % 2:
        money += ceil(bet/2)
        print("You almost won, you receive: ", ceil(bet/2), "$")
    else:
        money -= bet
        print("You lost:", bet)
    print("You have: ", money, "$")
    want_to_play = input("Do you want to keep on playing (y/n)?\n")
    if want_to_play == "n":
        out = True
        print("Thank you for playing with us!")
        
