from Die import *
from CrapsGame import *

def main():
    die1= Die(6)
    die2 = Die(6)
    game = CrapsGame()
    for i in range(5):
        print("")
        total = die1.roll() + die2.roll()
        if(game.processRoll(total) == 1):
            print("You rolled " + str(total) + ". You win!")
        elif(game.processRoll(total) == -1):
            print("You rolled " + str(total) + ". You lose.")
        else:
            print("You rolled " + str(total) + ". Let's see if you win!")
            total2 = die1.roll() + die2.roll()
            while(total2 != total and total2 != 7):
                print("You rolled " + str(total2) + ". Let's try again.")
                total2 = die1.roll() + die2.roll()
            if(total2 == total):
                print("You rolled " + str(total2) + ". You win!")
            else:
                print("You rolled 7. You lose.")
main()
