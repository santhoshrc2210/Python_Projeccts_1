# Mini-project #6 - Blackjack
#http://www.codeskulptor.org/#user47_TVapKMynPP_9.py
#run code in codeskulptor

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
in_play = 'False'
outcome = ""
score = 0

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
        self.cards=[]

    def __str__(self):
        a=''
        for p in self.cards:
            a+=str(p)+' '
        return 'Hand contains'+' '+a

    def add_card(self, card):
        self.card=card
        self.cards.append(card)

    def get_value(self):
        a=0
        b=[]
        c=0
        val=0
        hand_val=0
        for p in self.cards:
            a=p.get_rank()
            b.append(a)
            val+=VALUES[a]
            for i in b: #counting number of aces
                if i=='A':
                    c+=1
            if c==0:
                hand_val=val
            else:
                if val+10<=21:
                    hand_val=val+10
                else:
                    hand_val=val
        return hand_val    # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
                           # compute the value of the hand, see Blackjack video
    def draw(self, canvas, pos):
        for p in self.cards:
            a=p.get_rank()
            b=p.get_suit()
            card=Card(b,a)
            card.draw(canvas,pos)
            pos[0]=pos[0]+72


# define deck class
class Deck:
    def __init__(self):
        a=[]
        for s in SUITS:    # create a Deck object
            for r in RANKS:
                a.append(Card(s,r))
        self.deck=a

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        l= self.deck[-1]
        self.deck.pop()
        return l# deal a card object from the deck

    def __str__(self):
        a=''
        for p in self.deck:
            a+=str(p)+' '
        return 'Deck contains'+' '+a
                  # return a string representing the deck

#define event handlers for buttons
def deal():
    global outcome, in_play,deck,player,dealer,score
    if in_play=='False':
        deck=Deck() #create a deck of cards, global variable
        deck.shuffle() #shuffling the deck of cards created
        player=Hand() #create a player hand, global variable
        dealer=Hand() #create a dealer hand, global variable
        c1=deck.deal_card() #deal a card
        c2=deck.deal_card() #deal a card
        c3=deck.deal_card()
        c4=deck.deal_card()
        player.add_card(c1) #add card to player hand
        player.add_card(c3)
        print 'Player ' +str(player)
        dealer.add_card(c2) #add card to dealer hand
        dealer.add_card(c4)
        print 'Dealer ' +str(dealer)
        outcome='Hit or Stand?'
        in_play = 'True'
    else:
        score-=1
        outcome='Dealer wins'
        in_play='False'

def hit():
    global outcome,in_play,score
    val=player.get_value()  # replace with your code below
    if val<=21:
        c3=deck.deal_card() # if the hand is in play, hit the player
        player.add_card(c3)
        print 'Player ' +str(player)
        val2=player.get_value() # if busted, assign a message to outcome, update in_play and score
        if val2>21:
            outcome= 'You are busted'
            in_play='False'
            score-=1

def stand():
    global outcome,in_play,score
    val=player.get_value() # assign a message to outcome, update in_play and score
    if val>21:
        outcome= 'You are busted'
        in_play='False'
        score-=1
    else:
        val2=dealer.get_value()
        while val2<=17:              # if the hand is in play, hit the player
            c4=deck.deal_card()     # replace with your code below
            dealer.add_card(c4)
            val2=dealer.get_value()
            print 'Dealer ' +str(dealer)
        if val2>21:
            outcome= 'Dealer Busted'
            in_play='False'
            score+=1
# if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        elif val2>=val:
            outcome= 'Dealer wins'
            in_play='False'
            score-=1
        else:
            outcome= 'Player wins'
            in_play='False'
            score+=1

# draw handler
def draw(canvas):
    global outcome, in_play,score     # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (400, 50), 40, 'Red')
    canvas.draw_text('Score:'+str(score), (400, 100), 25, 'Black')
    #drawing dealer cards
    canvas.draw_text('Dealer', (100, 180), 25, 'Black')
    if in_play=='True':  #draw the flipped card for dealer
        dealer.draw(canvas,[100,200])
        card_loc = (CARD_BACK_CENTER[0]  ,
                    CARD_BACK_CENTER[1] )
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [100+0.5*CARD_BACK_SIZE[0] , 200+0.5*CARD_BACK_SIZE[1]], CARD_BACK_SIZE)
    else:  #open the card in the dealer
        dealer.draw(canvas,[100,200])
    #drawing player cards
    canvas.draw_text(outcome, (400, 380), 25, 'Black')
    canvas.draw_text('Player', (100, 380), 25, 'Black')
    player.draw(canvas,[100,400])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric
