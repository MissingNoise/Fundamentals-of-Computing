# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
num_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range
    if num_range == 1000:
        range1000()
    else:
        range100()



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global counter
    global num_range
    num_range = 100
    counter = 7
    secret_number = random.randrange(0,100)
    print "Guess a number [0, 100). You have 7 guesses."

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global counter
    global num_range
    counter = 10
    num_range = 1000
    secret_number = random.randrange(0,1000)
    print "Guess a number [0, 1000). You have 10 attempts."
    

# holds and prints out number of guess or retarts game if out of guesses.
def guess_counter():
    global counter
    if counter == 0:
        print "You are out of guesses! The correct number was " + str(secret_number) + "."
        print ""
        print "STARTING NEW GAME:"
        new_game()
    else:
        print "You have " + str(counter) + " attempt(s) left."
    
    
def input_guess(guess):
    # main game logic goes here	
    global counter
    guess = int(guess)
    print "Guess was " + str(guess) + "."

    # Compares guess to number
    if guess > secret_number:
        print "Lower!"
        counter -= 1
        guess_counter()
    elif guess < secret_number:
        print "Higher!"
        counter -= 1
        guess_counter()
    elif guess == secret_number:
        print "Correct!"
        print ""
        print "STARTING NEW GAME:"
        new_game()
    else:
        print "Bad input"
        
    print ""

    
# create frame
frame = simplegui.create_frame('Guess the number', 100, 200)
frame.add_input('Guess:', input_guess, 150)
frame.add_button('[0,100)', range100)
frame.add_button('[0,1000)', range1000)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
