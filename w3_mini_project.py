#http://www.codeskulptor.org/#user47_qehu2DM2zD_15.py
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# helper function to start and restart the game
def new_game():
    print "New game. Range is [0,100) \nNumber of remaining guesses is 7"
    new_game1(99)

def new_game1(range):
    global secret_number
    global num_guesses
    global rng
    rng= range
    secret_number=random.randint(0,range)
    if range==999:
        num_guesses=10
    elif range==99:
        num_guesses=7


# define event handlers for control panel
def range100():
    print "New game. Range is [0,100) \nNumber of remaining guesses is 7\n"
    new_game1(99)

def range1000():
    print "New game. Range is [0,1000) \nNumber of remaining guesses is 10\n"
    new_game1(999)


def input_guess(guess):
    global operand

    i=0
    global secret_number
    global num_guesses
    operand=int(guess)
    print "Guess was "+guess
    num_guesses=num_guesses-1
    if num_guesses==0:
        print "Number of remaining guesses is 0 \nYou ran out of guesses"
        print "The number was ",secret_number,"\n"
        i=i+1
        if rng==99:
            range100()
        elif rng==999:
            range1000()
    elif num_guesses>=1:
        print "Number of remaining guesses is "+str(num_guesses)
    if i>=1 and (num_guesses==10 or num_guesses==7):
        input_guess(guess)
    else:
        if secret_number<operand:
            print "Lower!\n"
        elif secret_number>operand:
            print "Higher!\n"
        else:
            print "Correct!\n"



# create frame
f = simplegui.create_frame("Guess the Number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)", range100, 100)
f.add_button("Range is [0,1000)", range1000,100)
f.add_input("Guess", input_guess, 100)

f.start()

# call new_game
new_game()
