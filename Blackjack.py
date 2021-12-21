#import random library
import random

print ("Blackjack!")
print ("====================")
#inital bank from the user
bank = int(input("How much money do you have? "))
print ("====================")

#variable to kick player out
win_streak = 0

while True:
    #getting the wager
    wager = int(input("How much would you like to wager: $"))
    while wager > bank:
        print ("You can't wager more than you have!")
        wager = int(input("How much would you like to wager: $"))

    #the users cards
    usercard1 = random.randint(2,11)
    usercard2 = random.randint(2,11)
    
    #the dealers cards
    dealercard1 = random.randint(2,11)
    dealercard2 =random.randint(2,11)
    if dealercard1 == 11 and dealercard2 == 11:
        dealercard2 = 1

    if usercard1 == 11:
        print ("Your first card was an ace!")
        usercard1 = int(input("Do you want the ace to be an 11 or a 1: "))
    

    if usercard2 == 11:
        print ("Your second card was an ace!")
        usercard2 = int(input("Do you want the ace to be an 11 or a 1: "))

    #calculating the current totals
    usertotal = usercard1+usercard2
    dealertotal = dealercard1 + dealercard2

    #telling the user what they have and one of the dealers cards
    print ("You drew", usercard1, "and", usercard2)
    print ("Your total is", usertotal)

    print ("The dealer has a", dealercard1)

    #does the user want to hit
    hit = int(input("Press 1 to hit, press any other number to hold: "))
    while hit == 1:
        #users next card
        newcard = random.randint(2,11)
        print ("You drew a", newcard)
        if usercard1 == 11 or usercard1 == 1:
            usercard1 = int(input("Would you like your ace to be a 1 or a 11: "))
        if usercard2 == 11 or usercard2 == 1:
            usercard2 = int(input("Would you like your ace to be a 1 or a 11: "))
        if newcard == 11 or newcard == 1:
            print ("It's an ace!")
            newcard = int(input("Would you like it to be a 1 or a 11: "))
        #adding the new card to their total
        usertotal += newcard
        #telling them what they have now
        print ("Your new total is", usertotal)
        #check if bust
        if usertotal > 21:
            print ("You busted!")
            break
        #ask if they want to hit again
        hit = int(input("Press 1 to hit, press any other number to hold: "))

    #the dealer hits while their score is less than 17
    while dealertotal < 17:
        newcard = random.randint (2,11)
        dealertotal += newcard
        if dealertotal > 21 and newcard == 11:
            dealertotal -= newcard
            newcard = 1
            dealertotal += newcard

    #tell the player what the dealer has
    print ("The dealer total is", dealertotal)
    
    #dealer wins
    if (dealertotal > usertotal and dealertotal <= 21) or usertotal > 21 or (dealertotal == usertotal and usertotal!= 21):
        print ("Dealer wins")
        bank = bank - wager
        print ("Your current balance is:", bank)
        win_streak = 0

    #player wins
    elif dealertotal < usertotal or dealertotal > 21:
        print ("You win!")
        if (usercard1 == 10 and usercard2 == 11) or (usercard1 == 11 and usercard2 == 10):
            bank = bank + wager*1.5
        else:
            bank = bank + wager
        print ("Your current balance is:", bank)
        win_streak += 1

    else:
        print ("Tie")
        print ("Your current balance is:", bank)

    #kick player out for winning too much
    if win_streak == 10:
        print ("We have reasonable suspicion that you are cheating, please leave immediately.")
        print ("Goodbye.")
        break

    #user runs out of money
    if bank == 0:
        print ("You ran out of money!")
        break

    #see if they want to play again
    run_status = int(input("Press 1 to play again, press any other number to quit: "))
    if run_status == 1:
        pass
    else:
        print ("Goodbye!")
        break
