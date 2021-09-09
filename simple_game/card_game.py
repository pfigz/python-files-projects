import random
import sys


help_file = "help.txt"
read_file = open(help_file, "r")
text = read_file.read()


def rules():
    get_rules = input("Type '--help' here to learn the rules: ")
    if get_rules == '--help':
        open(help_file, "r")
        print(text)
        resume = input('To exit and resume playing type \'--resume\' here: ')
        if resume == '--resume':
            read_file.close()
            pass
        elif resume != '--resume':
            rules()
    else:
        pass
        read_file.close()


rules()


class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        """Default constructor """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation """
        return '%s %s' % (Card.suits[self.suit], Card.ranks[self.rank])
        # return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        """Overriding < operator """
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        """Initializes the Deck with 52 cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Returns a string representation of the deck."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """Overriding len operator"""
        return len(self.cards)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def win_card(self, cards):
        """Get the highest winner card from list"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.win_count = 0

    def get_label(self):
        """ Store players name """
        return self.label

    def round_winner(self):
        """ increasing the win count for player """
        self.win_count += 1

    def get_win_count(self):
        """ get the winner count finally """
        return self.win_count

    # def __str__(self):
    #     return "Card's for " + self.label + " are " + Deck.__str__(self)


def play(argv):
    deck = Deck()  # initialize deck
    hands = []
    for i in range(1, 5):
        player = 'Player %d' % i  # default player name
        player_names = input(player + ' enter your name: ')
        if len(argv) > i:
            player_names = argv[i]  # get player name from command line parameter
        hands.append(Hand(player_names))  # add player

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())  # remove card from deck and add to hand

    # print(hands[0])  # print first player card
    input("Lets start playing. Press enter to continue")  # wait for keypress

    for i in range(1, 14):
        cards = []  # collect card in a round
        floors = []  # get string representation for display in each round
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)  # collect individual card
            floors.append(hand.get_label() + " : " + str(card))  # add string format for individual card

        winner_card = deck.win_card(cards)  # check for winner card
        winner_hand = hands[cards.index(winner_card)]  # find the winner hand from winner card
        winner_hand.round_winner()  # add score for winner hand
        print("Round", i, ":-", ", ".join(floors), ", Winner :- ", winner_hand.get_label(), ":", winner_card)
        input()  # wait for keypress to go for next round
        rules()

    for hand in hands:  # display the individual hand score after the 13 rounds of play
        print("Score for", hand.get_label(), "is", hand.get_win_count())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Play Again (Y/N)? : ")
    print("Bye Bye")


if __name__ == '__main__':
    main(sys.argv)
