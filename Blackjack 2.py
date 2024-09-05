# https://py2.codeskulptor.org/#user45_uVvGqEMQYI_0.py

# Project begun on 18/09/18
# Rules taken from https://www.pagat.com/banking/blackjack.html
# Five Card Charlie not in effect
# Dealer always stands on if > 17
# Player must draw onto minimum of 16

import simplegui
import random

# Constant values
BUTTON_SIZE  = 100
CARD_SPACING = 8
CARD_SIZE    = 72, 96
FRAME_SIZE   = 569, 600
FONT_SIZE    = 40
BET_RANGE    = [1, 5, 25, 100, 500]

image1 = simplegui.load_image('https://i.imgur.com/lKkv0Ga.png') # Cards
image2 = simplegui.load_image('https://i.imgur.com/m3M7jDp.png') # Card Back
image3 = simplegui.load_image('https://i.imgur.com/mOSzWGM.png') # Chips

message1 = "Player and Dealer Blackjack"
message2 = "Dealer wins"
message3 = "Player wins"
message4 = "Both Player and Dealer bust"
message5 = "Dealer bust, Player wins"
message6 = "Player bust, Dealer wins"
message7 = "Dealer has Blackjack"
message8 = "Player has Blackjack"
message9 = "Tie, Push"

"""
# Tester 
print "####################"
print "Player_score       : ", player_score
print "Dealer_score       : ", dealer_score
print "player_hand        : ", player_hand
print "dealer_hand        : ", dealer_hand
print "deck               : ", deck
print "player_hand        : ", len(player_hand)
print "dealer_hand        : ", len(dealer_hand)
"""

def deal_handler():
    if gamestate == 0:
        game_start()

def hit_handler():
    global betting
    if gamestate == 1:
        # Prevent increase / decrease betting after game begun
        betting = False
        
        # Add 1 card to player hand
        player_brain.add_card_into_hand()

        # Update score
        player_count_score.calculate()
        
        # Check bust
        if player_score > 21:
            # Dealer's turn
            stand_handler()
                      
def stand_handler():
    global gamestate
    if gamestate == 1:
        if player_score > 15:
            while dealer_score < 17:
                # Dealer draws card
                dealer_brain.add_card_into_hand()

                # Update dealer score
                dealer_count_score.calculate()
            gamestate = 0
            
def increase_handler():
    global bet
    if betting == True:
        for i in range(0, len(BET_RANGE), 1):
            if bet == BET_RANGE[i]:
                # Don't increase if maxed out already
                if i + 1 != len(BET_RANGE):
                    bet = BET_RANGE[i + 1]
                    break
                
def decrease_handler():
    global bet
    if betting == True:
        for i in range(0, len(BET_RANGE), 1):
            if bet == BET_RANGE[i]:
                # Don't decrease if maxed out already
                if i - 1 != -1:
                    bet = BET_RANGE[i - 1]
                    break
            
class Brain:
    def __init__(self, name):
        self.name = name

    def get_card_X(self, num):
        self.number = deck[51 - num][0]
        self.card_X = (self.number - 1) * 72 + 36
        return self.card_X
    
    def get_card_Y(self, num):
        suit = deck[51 - num][1]
        if suit == 1:
            self.card_Y = 48
        elif suit == 2:
            self.card_Y = 144
        elif suit == 3:
            self.card_Y = 240
        elif suit == 4:
            self.card_Y = 336
        return self.card_Y
    
    def add_card_into_hand(self):
        global remaining_card
        # Create Unique number, suit, card_order
        self.number     = deck[remaining_card][0]
        self.suit       = deck[remaining_card][1]
        self.card_order = 51 - remaining_card
        if   self.name == "player":
            player_hand.append([self.number, self.suit, self.card_order])
        elif self.name == "dealer":
            dealer_hand.append([self.number, self.suit, self.card_order])
        
        remaining_card -= 1

class Card_handler:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def draw_card(self, canvas):
        width_height_source = CARD_SIZE[0], CARD_SIZE[1]
        width_height_dest   = CARD_SIZE[0], CARD_SIZE[1]
        self.hand_length = len(self.hand)
        for i in range(0, self.hand_length, 1):
                # First row
                card_order = self.hand[i][2]
                if   self.name == "player":
                    center_source = player_brain.get_card_X(card_order), player_brain.get_card_Y(card_order)
                    center_dest   = CARD_SPACING + CARD_SIZE[0] / 2  + (CARD_SIZE[0] + CARD_SPACING) * i, FRAME_SIZE[1] - 60           
                elif self.name == "dealer":
                    center_source = dealer_brain.get_card_X(card_order), dealer_brain.get_card_Y(card_order)
                    center_dest   = CARD_SPACING + CARD_SIZE[0] / 2  + (CARD_SIZE[0] + CARD_SPACING) * i, 60           
                canvas.draw_image(image1, center_source, width_height_source, center_dest, width_height_dest)
                
                # Second row
                if self.hand_length >= 6:
                    if   self.name == "player":
                        center_dest   = CARD_SPACING + CARD_SIZE[0] / 2  + (CARD_SIZE[0] + CARD_SPACING) * (i - 7), FRAME_SIZE[1] - 170          
                    elif self.name == "dealer":
                        center_dest   = CARD_SPACING + CARD_SIZE[0] / 2  + (CARD_SIZE[0] + CARD_SPACING) * (i - 7), 170         
                    canvas.draw_image(image1, center_source, width_height_source, center_dest, width_height_dest)   

class Count_score:
    def __init__(self, name, hand):
        self.name  = name
        self.hand  = hand
        
    def calculate(self):
        global dealer_score, player_score
        self.score = 0
        self.ace = 0
        for i in self.hand:
            # Jack, Queen, King value 10
            if   i[0] > 10:
                self.score += 10
            # First assume ace value is 11
            elif i[0] == 1:
                self.ace += 1
                self.score += 11
            # Normal card
            else:
                self.score += i[0]
            # Check if bust
        if self.score > 21:
            for i in self.hand:
                # Convert ace back to 1, one at a time
                if i[0] == 1:
                    self.score -= 10
                    # Stop converting when no longer bust
                    if self.score < 21:
                        break
        if   self.name == "player":
            player_score = self.score
        elif self.name == "dealer":
            dealer_score = self.score
            
def shuffle():
    while(len(deck) < 52):
        # Reset exist
        exist = False
        
        # Suit randomizer
        suit   = random.randint(1, 4)
        
        # Number randomizer
        number = random.randint(1, 13)
        
        # New Card
        generated_card = [number, suit]
        
        # Check if card already in deck
        for i in deck:
            if(i == generated_card):
                exist = True
        
        # If card is new, add into deck
        if exist == False:
            deck.append(generated_card)
            
def main():
    global dealer_brain, dealer_score
    global player_brain, player_score
    global bet, money
    
    # Variable declaration
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    
    # Initial money
    bet = BET_RANGE[0]
    money = 1000
    
    # Class assignments
    player_brain = Brain("player")
    dealer_brain = Brain("dealer")
    
def game_start():
    # Declare global variables
    global betting, deck, gamestate, remaining_card
    global player_blackjack, player_count_score, player_hand, player_score
    global dealer_blackjack, dealer_count_score, dealer_hand, dealer_score
    
    # Reset values
    betting = True
    deck = []
    gamestate = True
    remaining_card = 51
    player_blackjack = False
    dealer_blackjack = False
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    
    # Create deck
    shuffle()
    
    # Player and dealer draws 2 cards each
    player_brain.add_card_into_hand()
    dealer_brain.add_card_into_hand()
    player_brain.add_card_into_hand()
    dealer_brain.add_card_into_hand()
    
    # Class assignment
    player_count_score = Count_score("player", player_hand)
    dealer_count_score = Count_score("dealer", dealer_hand)

    # Update score
    player_count_score.calculate()
    dealer_count_score.calculate()
    
    # Check for Blackjack
    if player_hand[0][0] == 1 and player_hand[1][0] == 1:
        player_blackjack = True
    if dealer_hand[0][0] == 1 and dealer_hand[1][0] == 1:
        dealer_blackjack = True
    if player_blackjack == True or dealer_blackjack == True:
        gamestate = False

def game_over(canvas):
    if gamestate == False:
        # Default color
        font_color = "Black"
        
        # Determine winner assuming neither busted
        if   dealer_score == player_score:
            message = message9
        elif dealer_score > player_score:
            message = message2
        elif player_score > dealer_score:
            message = message3

        # Determine if player or dealer busted
        if dealer_score > 21 and player_score > 21:
            message = message4
        elif dealer_score > 21:
            message = message5
        elif player_score > 21:
            message = message6
        
        # If either player or dealer has blackjack
        if dealer_blackjack == True and player_blackjack == True:
            message = message1
            font_color = "Red"
        elif dealer_blackjack == 1:
            message = message7
        elif player_blackjack == 1:
            message = message8
            money  = money / 2 * 3
            
        # Calculating money
        # Player win
        if   message == message3 or message == message5:
            money += bet
        # Dealer win
        elif message == message2 or message == message6:
            money -= bet
        
            
            
        # Draw end game text
        canvas.draw_text(message, (0, FRAME_SIZE[1] / 2 - 40), FONT_SIZE, font_color)
    
def draw_handler(canvas):
    # Draw Cards
    Card_handler("player", player_hand).draw_card(canvas)
    Card_handler("dealer", dealer_hand).draw_card(canvas)
    
    # If game is over, remove dealer cover
    if   gamestate == True:
        canvas.draw_image(image2, (35.5, 48), (71, 96), (124, 60), (72, 96))
    
    # Draw bet
    canvas.draw_text("Bet: " + str(bet), (0, FRAME_SIZE[1] / 2), FONT_SIZE, "Black")

    
    # Draw money
    canvas.draw_text("$ " + str(money), (0, FRAME_SIZE[1] / 2 + 40), FONT_SIZE, "Black")

    # Initializer
    game_over(canvas)
        
# Initializer
main()
game_start()

frame = simplegui.create_frame("Blackjack", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_canvas_background("Green")
frame.set_draw_handler(draw_handler)
button1 = frame.add_button("Deal",         deal_handler    , BUTTON_SIZE)
button2 = frame.add_button("Hit",          hit_handler     , BUTTON_SIZE)
button3 = frame.add_button("Stand",        stand_handler   , BUTTON_SIZE)
button4 = frame.add_button("Increase bet", increase_handler, BUTTON_SIZE)
button5 = frame.add_button("Decrease bet", decrease_handler, BUTTON_SIZE)

frame.start()
