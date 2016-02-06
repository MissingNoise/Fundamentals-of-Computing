# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
Startgame = False
dealerWins = 0
playerWins = 0
outcome = "Press deal to start game"


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = list()

    def __str__(self):
        ans = []
        for i in self.hand:
            ans += [i.get_suit() + i.get_rank()]
        return "hand contains " + " ".join(ans)
        

    def add_card(self, card):
        self.hand.append(card)
        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value = 0
        aces = False
        for n in self.hand:
            if "A" == n.get_rank():
                aces = True
        for i in self.hand:
            value += VALUES[i.get_rank()]
        if value + 10 <= 21 and aces:
            value = value + 10
        return value
            
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards

# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        ans = []
        for i in self.deck:
            ans += [i.get_suit() + i.get_rank()]
        return "Deck contains %s" %" ".join(ans)


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer, player, dealerWins, Startgame, dealerC, playerC
    deck = Deck()
    player = Hand()
    dealer = Hand()
    dealerC = ""
    playerC = ""
    if Startgame:
        deck.shuffle()
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        outcome = "Hit or stand?"
        playerC = str(player.get_value())
        if in_play:
            dealerWins += 1
        in_play = True
        if dealer.get_value() == 21:
            outcome = "Dealer has 21. You lose."
            dealerC = str(dealer.get_value())
            in_play = False
            dealerWins += 1
    Startgame = True
    
    
def hit():
    global in_play, player, deck, outcome, dealerWins, playerC
    # if the hand is in play, hit the player
    if in_play and player.get_value() <= 21:
        player.add_card(deck.deal_card())
        outcome = "Hit or stand?"
        playerC = str(player.get_value())
        if player.get_value() > 21:
            outcome = "Bust! New deal?"
            dealerWins += 1
            in_play = False
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global in_play, deck, dealer, outcome, dealerWins, playerWins, dealerC
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if player.get_value() > 21:
        outcome = "Already bust! New deal?"
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            playerWins += 1
            outcome = "Dealer bust. New deal?"
            in_play = False
        dealerC = str(dealer.get_value())
    # assign a message to outcome, update in_play and score
    if in_play and dealer.get_value() >= player.get_value():
        outcome = str(dealer.get_value()) + " >= " + str(player.get_value()) + " Player Loses. New deal?"
        dealerWins += 1
    elif in_play:
        outcome = str(dealer.get_value()) + " < " + str(player.get_value()) + " Player wins! New deal?"
        playerWins += 1
    in_play = False
    
    
# draw handler    
def draw(canvas):
    for dk in range(len(deck.deck)):
        if dk == len(deck.deck) - 1:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [580, dk * 2 + CARD_BACK_SIZE[1] + 10], CARD_BACK_SIZE)
        else:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [580, dk * 2 + CARD_BACK_SIZE[1]], CARD_BACK_SIZE)
              
    for p in range(len(player.hand)):
        player.hand[p].draw(canvas, [(p * CARD_SIZE[0] + 40), (490 - CARD_SIZE[1])])
        
    for d in range(len(dealer.hand)):
        if in_play:
            dealer.hand[1].draw(canvas, [40, 110])
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [CARD_BACK_CENTER[0] + 60, CARD_BACK_CENTER[0] + 130], CARD_BACK_SIZE)
        else:
            dealer.hand[d].draw(canvas, [(d * CARD_SIZE[0] + 40), 110])
            
    canvas.draw_text(outcome, (30, 310), 22, 'White', 'monospace')
    canvas.draw_text("Dealer: " + str(dealerWins), (10, CARD_SIZE[1] + 140), 22, 'MintCream', 'monospace')
    canvas.draw_text("Player: " + str(playerWins), (10, 475 - CARD_SIZE[1]), 22, 'MintCream', 'monospace')
    canvas.draw_text("Dealer Hand: " + dealerC, (200, CARD_SIZE[1] + 140), 22, 'MintCream', 'monospace')
    canvas.draw_text("Player Hand: " + playerC, (200, 475 - CARD_SIZE[1]), 22, 'MintCream', 'monospace')
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("DarkBlue")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric