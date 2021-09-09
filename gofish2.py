#Go fish example 2

import random

def MakeDeck():
    deck = []
    c = 0
    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Spades", "Diamonds", "Clubs"]

    for v in values:
        for s in suits:
            deck.append([v,s])

    random.shuffle(deck)

    return deck





import random, time

fish_deck = deck.MakeDeck()

#for i in fish_deck:
#    print(i[0]+" of "+i[1])

class fisherman():
    name = ""
    hand = []
    sets = []

def ask(player1, player2):
    pause = random.randint(2,5)
    has = []
    choose = randint(0,len(player1.hand)-1)
    value = player1.hand[choose][0]
    for card in player2.hand:
        if card[0] == value:
        has.append(card)
    for card in has:
        player2.hand.remove(card)
    for card in has:
        player1.hand.append(card)
    return_string = player1.name+" asked "+player2.name+" for "+value+"s. "
    print(return_string)
    return_string = player2.name+" had "+str(len(has))+". "
    print(return_string)
    if len(has) == 0:
        draw(player1)
        return_string = player1.name+" had to go fish."
    print(return_string)

def draw(player):
    card = fish_deck.pop()
    player.hand.append(card)

def set_check(player):
    amount = {}
    for card in player.hand:
        if card[0] not in amount.keys():
            amount[card[0]] = 1
        if card[0] in amount.keys():
            amount[card[0]] += 1
    for count in amount.keys():
        if amount[count] == 4:
            print(player.name+" got a set of "+count+"s.")
            player.sets.append(count)
            player.hand[:] = [card for card in player.hand if card[0] == count]

john = fisherman()
john.name = "John"
tim = fisherman()
tim.name = "Tim"
sara = fisherman()
sara.name = "Sara"
kris = fisherman()
kris.name = "Kris"

def play(player1, player2, player3, player4, deck):
    turn = 0
    size = 7
    dealt = 0
    order = [player1, player2, player3, player4]
    random.shuffle(order)
    while dealt < size:
        draw(order[0])
        draw(order[1])
        draw(order[2])
        draw(order[3])
        dealt += 1
    while len(deck) != 0:
        for player in order:
            count = 0
            hand = player.name+"'s hand: "
            for card in player.hand:
                if count < len(player.hand)-1:
                    hand += card[0]+" of "+card[1]+", "
                    count += 1
                elif count == len(player.hand)-1:
                    hand += card[0]+" of "+card[1]+"."
            print(hand)
            count = 0
            sets = player.name+"'s sets: "
            for set in player.sets:
                if count < len(player.sets)-1:
                    sets += set+"s, "
                elif count == len(player.sets)-1:
                    sets += set+"s."
            print(sets)
        other_player = turn
        while other_player == turn:
            other_player = random.randint(0,3)
        ask(order[turn], order[other_player])
        set_check(order[turn])
        if turn >= 3:
            turn = 0
        else:
            turn += 1
        time.sleep(10)
        print("=========================================")

play(john, tim, sara, kris, fish_deck)