__author__ = 'Kevin'
# save testing 2
import random
import time


def get_players():
    number_of_players = int(input("how many people are playing?"))
    players = []  # list of players
    while len(players) < number_of_players:
        players.append([])  # adds empty sets for each player in the game
    return players


def deal_cards(players, deck):
    count_cards = 0
    cards_per_person = int(input("how many starting cards per player"))

    while count_cards < cards_per_person:  # while loop gives cards from deck to players
        current_player = 0
        while current_player < len(players):
            temp_card = random.randint(0, len(deck) - 1)
            players[current_player].append(deck[temp_card])
            deck.remove(deck[temp_card])
            current_player += 1

        count_cards += 1

    return players


def give_cards(deck, players, player_turn, cardeffect):
    temp_card = random.randint(0, len(deck) - 1)
    players[player_turn].append(deck[temp_card])
    deck.remove(deck[temp_card])

    return players, deck


def place_cards(players, playerturn, deck, pile, first_go, cardeffect):
    card_choice = int(input("pick a card (the leftmost card being 1): ")) - 1
    valid, first_go = checkcard(pile, players, playerturn, card_choice, first_go, deck, cardeffect)
    if valid:
        print("this is a valid card")
        pile.append(players[playerturn][card_choice])
        players[playerturn].remove(players[playerturn][card_choice])
        players, pile, deck = turn(playerturn, players, deck, pile, cardeffect, first_go)
    return pile, players


def checkcard(pile, players, playerturn, cardchoice, firstgo, deck, cardeffect):
    print("checking if choice is valid...")
    time.sleep(2)
    valid = False

    if firstgo:

        if players[playerturn][cardchoice][0] == pile[len(pile) - 1][0]:
            valid = True
            firstgo = False

        elif players[playerturn][cardchoice][1] == pile[len(pile) - 1][1]:
            valid = True
            firstgo = False

        else:
            valid = False

        if valid == False:
            print("this is not a valid choice, please try again")
            players, pile, deck = turn(playerturn, players, deck, pile, cardeffect, firstgo)

    else:

        if players[playerturn][cardchoice][0] == "jack":
            if (pile[len(pile) - 1][0] == 10 or "queen" or "jack") and players[playerturn][cardchoice][1] == \
                    pile[len(pile) - 1][1]:
                valid = True

            else:
                valid = False

        elif players[playerturn][cardchoice][0] == "queen":
            if (pile[len(pile) - 1][0] == "jack" or "king" or "queen") and players[playerturn][cardchoice][1] == \
                    pile[len(pile) - 1][1]:
                valid = True
            else:
                valid = False

        elif players[playerturn][cardchoice][0] == "king":
            if (pile[len(pile) - 1][0] == 1 or "queen" or "king") and players[playerturn][cardchoice][1] == \
                    pile[len(pile) - 1][1]:
                valid = True
            else:
                valid = False

        elif players[playerturn][cardchoice][0] == 10:
            if (pile[len(pile) - 1][0] == 9 or "jack" or 10) and players[playerturn][cardchoice][1] == \
                    pile[len(pile) - 1][1]:
                valid = True
            else:
                valid = False

        elif players[playerturn][cardchoice][0] == 1:
            if (pile[len(pile) - 1][0] == 2 or "king" or 1) and players[playerturn][cardchoice][1] == \
                    pile[len(pile) - 1][1]:
                valid = True
            else:
                valid = False

        elif players[playerturn][cardchoice][0] == pile[len(pile) - 1][0]:
            valid = True
        elif players[playerturn][cardchoice][0] == pile[len(pile) - 1][0] + 1 and players[playerturn][cardchoice][1] == \
                pile[len(pile) - 1][1]:
            valid = True
        elif players[playerturn][cardchoice][0] == pile[len(pile) - 1][0] - 1 and players[playerturn][cardchoice][1] == \
                pile[len(pile) - 1][1]:
            valid = True
        else:

            valid = False

    if valid == False and firstgo == False:
        print("this is not a valid choice")
        choice = int(input("press 1 to try again or 2 to end go"))
        if choice == 1:
            pile, players = place_cards(players, playerturn, deck, pile, firstgo, cardeffect)
        else:
            pass

    return valid, firstgo


def turn(playerturn, players, deck, pile, cardeffect, firstgo):
    print("The current card ontop of the pile is:", pile[len(pile) - 1])
    print("player", playerturn + 1, "has these cards:", players[playerturn])
    if firstgo:

        print("what would you like to do?: ")
        print("1. place a card")
        print("2. pickup a card")
        choice = int(input("choice : "))
        if choice == 1:
            pile, players = place_cards(players, playerturn, deck, pile, firstgo, cardeffect)
        else:
            players, deck = give_cards(deck, players, playerturn, cardeffect)

    else:
        print("what would you like to do?: ")
        print("1. place a card")
        print("2. end turn")
        choice = int(input("choice : "))
        if choice == 1:
            # noinspection PyTypeChecker
            pile, players = place_cards(players, playerturn, deck, pile, firstgo, cardeffect)
        else:
            pass

    return players, pile, deck


def cardeffect(cardnumber, playerturn):
    print()


def gameloop(start, end, step, playerturn, deck, players, pile):
    while start <= end - 1:
        playerturn = start
        firstgo = True
        players, pile, deck = turn(playerturn, players, deck, pile, cardeffect, firstgo)
        start += step
        if start == end:
            start = 0
        if start < 0:
            start = len(players) - 1
        if step >= 2:
            step = 1
        if step <= -2:
            step = 1


deck = [[1, "hearts"], [1, "diamonds"], [1, "spades"], [1, "clubs"],
        [2, "hearts"], [2, "diamonds"], [2, "spades"], [2, "clubs"],
        [3, "hearts"], [3, "diamonds"], [3, "spades"], [3, "clubs"],
        [4, "hearts"], [4, "diamonds"], [4, "spades"], [4, "clubs"],
        [5, "hearts"], [5, "diamonds"], [5, "spades"], [5, "clubs"],
        [6, "hearts"], [6, "diamonds"], [6, "spades"], [6, "clubs"],
        [7, "hearts"], [7, "diamonds"], [7, "spades"], [7, "clubs"],
        [8, "hearts"], [8, "diamonds"], [8, "spades"], [8, "clubs"],
        [9, "hearts"], [9, "diamonds"], [9, "spades"], [9, "clubs"],
        [10, "hearts"], [10, "diamonds"], [10, "spades"], [10, "clubs"],
        ["jack", "hearts"], ["jack", "diamonds"], ["jack", "spades"], ["jack", "clubs"],
        ["queen", "hearts"], ["queen", "diamonds"], ["queen", "spades"], ["queen", "clubs"],
        ["king", "hearts"], ["king", "diamonds"], ["king", "spades"], ["king", "clubs"]]

pile = []

players = get_players()

players = deal_cards(players, deck)

pile.append(deck[random.randint(0, len(deck) - 1)])

gameloop(0, len(players), 1, 0, deck, players, pile)
