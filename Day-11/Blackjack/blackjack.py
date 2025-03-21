import random

# Kelas untuk kartu
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11  # Aces can be 1 or 11, handled later
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Kelas untuk dek
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Kelas untuk pemain
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def hand_value(self):
        value = sum(card.value() for card in self.hand)
        # Adjust for Aces
        aces = sum(1 for card in self.hand if card.rank == 'A')
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    def __str__(self):
        return f"{self.name}'s hand: " + ', '.join(str(card) for card in self.hand)

# Kelas untuk permainan Blackjack
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def initial_deal(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())

    def display_hands(self, reveal_dealer=False):
        print(self.player)
        if reveal_dealer:
            print(self.dealer)
        else:
            print(f"Dealer's hand: {self.dealer.hand[0]}, [Hidden]")

    def player_turn(self):
        while True:
            self.display_hands()
            if self.player.hand_value() > 21:
                print("Player busts! Dealer wins.")
                return False
            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == 'h':
                self.player.add_card(self.deck.deal_card())
            elif action == 's':
