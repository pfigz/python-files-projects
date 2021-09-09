# Blackjack Part A, B, C, D, E, F
from random import shuffle
import itertools


def create_deck():
    deck = []

    face_values = ["A", "J", "Q", "K"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for i in range(4): # 4 different suits
        for card in range(2, 11): #adding cards 2-10
            deck.append(str(card))
        for s in suits:
            deck.append(s)


        for card in face_values:
            deck.append(card)


    shuffle(deck)
    return deck

##new_deck = create_deck()
#print(new_deck)
class Player:

    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0

    def __str__(self): # print(Player)
        current_hand = "" #self.hand = ["A", "10"]
                            # "A 10"
        for card in self.hand:
            current_hand += str(card) + " "
        final_status = current_hand + "score: " + str(self.score)
        #"A 10 2 4 score: 17"
        return  final_status

    def set_score(self):
        self.score = 0
        face_cards_dict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                           "2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7":7, "8":8, "9":9, "10":10}
        ace_counter = 0
        for card in self.hand: #"10"
                self.score += face_cards_dict[card]
                if card == "A":
                    ace_counter += 1
                if self.score > 21 and ace_counter != 0:
                    self.score -= 10
                    ace_counter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.set_score()

    def play(self, new_hand):
        self.hand = new_hand
        self.score = self.set_score()

    def bet_amount(self, amount):
        self.money -= amount # money 100; bet 20
        self.bet += amount # money 100 ->80, bet 0->20

    def win(self, result):
        if result == True:
            if self.score == 21:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def has_blackjack(self):
        if self.score == 21:
            return True
        else:
            False


def print_house(house):
    for card in range(len(house.hand)):
        if card == 0:
            print("X", end = " ")
        elif card == len(house.hand) - 1:
            print(house.hand[card])
        else:
            print(house.hand[card], "H", end = " ")

card_deck = create_deck()


first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]
player1 = Player(first_hand)
house = Player(second_hand)
card_deck = create_deck()
while True:
    if len(card_deck) < 20:
        card_deck = create_deck()
    first_hand = [card_deck.pop(), card_deck.pop()]
    second_hand = [card_deck.pop(), card_deck.pop()]
    player1.play(first_hand)
    house.play(second_hand)

    bet = int(input("Enter your bet: "))

    player1.bet_amount((bet))

    print(card_deck)
    print_house(house)
    print(player1, "P")

    if player1.has_blackjack():
        if house.has_blackjack():
            player1.draw()
        else:
            player1.win(True)
    else:
        while(player1.score < 21):
            action = input("Do you want another card?(y/n): ")
            if action == "y":
                player1.hit(card_deck.pop())
                print(player1, "P")
                print(house, "H")
            else:
                break
        while(house.score < 16):
            print(house, "H")
            house.hit(card_deck.pop())

        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(False)
        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                player1.win(False)

    print(player1.money)
    print(house, "H")

