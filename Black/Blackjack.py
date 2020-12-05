import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        total_cards = ' '
        for card in self.deck:
            total_cards += '\n' + card.__str__()
        return total_cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.suit == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(Chips):
    while True:

        try:
            Chips.bet = int(input("Enter the chips for betting : "))
        except:
            print("Sorry plz provide the valied input !!!")
        else:
            if Chips.bet > Chips.total:
                print(f"Your chips are low for betting, check your available balance {Chips.total}")
                continue

            else:
                print("Your chips was concidered and betting was taken place ")
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("You player would like to take hit or stand either h or s ? :")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0] == 's':
            print("Player wants to stand and it's dealers turns...")
            playing = False
        else:
            print("plz provide the correct info !!!!")
            continue
        break


def show_some(player, dealer):
    print("Dealer cards ::::::")
    print(f"<<CARD HIDDEN>>     {dealer.cards[1]}")
    #     print(dealer.cards[1])
    print("Player cards ::::::")
    for each_card in player.cards:
        print(each_card)
    print("Player Cards value :", player.value)


def show_all(player, dealer):
    print("Dealer cards ::::::")
    for each_card in dealer.cards:
        print(each_card)
    print("Dealer Cards value :", dealer.value)

    #
    print("Player cards ::::::")
    for each_card in player.cards:
        print(each_card)
    print("Player Cards value :", player.value)


def player_busts(player, dealer, chips):
    print("Dealer WINS")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer got busted and PLAYER WINS")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Player got busted and DEALER WINS")
    chips.lose_bet()


def push(player, dealer):
    print("Player and dealer got tie !!!")


while True:
    # Print an opening statement
    print("WELCOME TO THE BLACKJACK")

    # Create & shuffle the deck, deal two cards to each player
    mydeck = Deck()
    mydeck.shuffle()

    player_hand = Hand()
    player_hand.add_card(mydeck.deal())
    player_hand.add_card(mydeck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(mydeck.deal())
    dealer_hand.add_card(mydeck.deal())
    # Set up the Player's chips
    player_chips = Chips()
    take_bet(player_chips)
    # Prompt the Player for their bet
    print("Congratulations player")
    print("Your chips as successfully collected to our company and BEST OF LUCK 4U ")

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(mydeck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(mydeck, dealer_hand)
        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value >= 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif player_hand.value < dealer_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"Now your total chips available in your bank balance : {player_chips.total}")
    # Ask to play again
    game = input("Enter for keep playing Y/N ? :")
    if game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("TQs for playing ....!!!")
        break