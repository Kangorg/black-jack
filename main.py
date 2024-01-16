import random

class Deck:
    def __init__(self):
        self.__deck = {
            'Diamonds': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Hearts': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Spades': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Clubs': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        }

    def get_card_deck(self, suit, card):
        suit_holder = self.__deck[suit]
        card_index_holder = suit_holder.index(card)
        card_value = suit_holder.pop(card_index_holder)
        return card_value

    def is_card_there(self, suit, card):
        suit_holder = self.__deck[suit]
        try:
            card_index_holder = suit_holder.index(card)
            if suit_holder[card_index_holder] == card:
                return True
            else:
                return False
        except:
            return False

    def card_count(self):
        card_amount = 0
        for cards in self.__deck.values():
            card_amount += len(cards)
        return card_amount

    def get_deck(self):
        return self.__deck

    def shuffle(self):
        self.__deck = {
            'Diamonds': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Hearts': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Spades': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'],
            'Clubs': [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        }


class Shoe(Deck):
    def __init__(self):
        self.__shoe = []
        while len(self.__shoe) < 6:
            make_deck = Deck()
            self.__shoe.append(make_deck)

    def get_card_shoe(self):
        run_again = True
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        suit = suits[random.randint(0, 3)]
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        card = cards[random.randint(0, 12)]
        while run_again:
            for deck in self.__shoe:
                if deck.is_card_there(suit, card):
                    card_value = deck.get_card_deck(suit, card)
                    run_again = False
                    return card_value
                else:
                    suit = suits[random.randint(0, 3)]
                    card = cards[random.randint(0, 12)]
                    continue

    def get_shoe(self):
        for decks in self.__shoe:
            print(decks.get_deck())

    def shoe_card_count(self):
        shoe_card_amount = 0
        for decks in self.__shoe:
            shoe_card_amount += decks.card_count()
        return shoe_card_amount

    def shoe_shuffle(self):
        for decks in self.__shoe:
            decks.shuffle()


class Player:
    def __init__(self):
        self.__winnings = 0
        self.__hand = []

    def hit(self, card):
        self.__hand.append(card)

    def get_hand(self):
        print('Your hand:', end=' ')
        for cards in self.__hand:
            print(f'{cards},', end=' ')
        print('')

    def get_hand_value(self):
        hand_value = 0
        alt_hand_value = 0
        for cards in self.__hand:
            if (cards == 'Jack') or (cards == 'Queen') or (cards == 'King'):
                hand_value += 10
                alt_hand_value += 10
            elif (cards == 'Ace'):
                hand_value += 11
                alt_hand_value += 1
            else:
                hand_value += cards
                alt_hand_value += cards
        values = [hand_value, alt_hand_value]
        return values

    def clear_hand(self):
        self.__hand.clear()

    def is_over_21(self):
        hand = self.get_hand_value()
        if (hand[0] > 21) and (hand[1] > 21):
            return True
        else:
            return False

    def is_21(self):
        hand = self.get_hand_value()
        if (hand[0] == 21) or (hand[1] == 21):
            return True
        else:
            return False

    def is_hand_greater(self, amount):
        hand = self.get_hand_value()
        if ((hand[0] > amount[0]) and (hand[0] > amount[1])) or ((hand[1] > amount[0]) and (hand[1] > amount[1])):
            return True
        else:
            return False

    def add_winnings(self, amount):
        self.__winnings += amount

    def lose_winnings(self, amount):
        self.__winnings -= amount

    def get_winnings(self):
        return self.__winnings


class Dealer:
    def __init__(self):
        self.__hand = []

    def hit_dealer(self, card):
        self.__hand.append(card)

    def first_card(self):
        for cards in self.__hand:
            return cards

    def get_dealer_hand(self):
        print('Dealer hand:', end=' ')
        for cards in self.__hand:
            print(f'{cards},', end=' ')
        print('')

    def get_dealer_hand_value(self):
        hand_value = 0
        alt_hand_value = 0
        for cards in self.__hand:
            if (cards == 'Jack') or (cards == 'Queen') or (cards == 'King'):
                hand_value += 10
                alt_hand_value += 10
            elif cards == 'Ace':
                hand_value += 11
                alt_hand_value += 1
            else:
                hand_value += cards
                alt_hand_value += cards
        values = [hand_value, alt_hand_value]
        return values

    def is_dealer_over_21(self):
        hand = self.get_dealer_hand_value()
        if (hand[0] > 21) and (hand[1] > 21):
            return True
        else:
            return False

    def is_dealer_21(self):
        hand = self.get_dealer_hand_value()
        if (hand[0] == 21) or (hand[1] == 21):
            return True
        else:
            return False

    def is_dealer_hand_greater(self, amount):
        hand = self.get_dealer_hand_value()
        if ((hand[0] > amount[0]) and (hand[0] > amount[1])) or ((hand[1] > amount[0]) and (hand[1] > amount[1])):
            return True
        else:
            return False

    def clear_dealer_hand(self):
        self.__hand.clear()

#This plays the blackjack game
the_shoe = Shoe()
jake = Dealer()
tim = Player()
play_game = input("Enter 'play' to play blackjack.\n")
while play_game == 'play':
    game_over = False
    jake.clear_dealer_hand()
    tim.clear_hand()
    if the_shoe.shoe_card_count() < 100:
        the_shoe.shoe_shuffle()
    card1 = the_shoe.get_card_shoe()
    tim.hit(card1)
    card2 = the_shoe.get_card_shoe()
    jake.hit_dealer(card2)
    card3 = the_shoe.get_card_shoe()
    tim.hit(card3)
    card4 = the_shoe.get_card_shoe()
    jake.hit_dealer(card4)
    print("Dealer's card showing:", jake.first_card())
    tim.get_hand()
    player_hand_value = tim.get_hand_value()
    dealer_hand_value = jake.get_dealer_hand_value()
    if (tim.is_21()) and (jake.is_dealer_21()):
        print('Tie! Both have Natural Blackjack!')
        tim.get_hand()
        jake.get_dealer_hand()
        print(f'Current winnings: ${tim.get_winnings()}')
        play_game = input("Enter 'play' to keep playing blackjack.\n")
        continue
    elif jake.is_dealer_21():
        print('Dealer wins! Natural Blackjack!')
        tim.get_hand()
        jake.get_dealer_hand()
        tim.lose_winnings(1)
        print(f'Current winnings: ${tim.get_winnings()}')
        play_game = input("Enter 'play' to keep playing blackjack.\n")
        continue
    elif tim.is_21():
        print('Player wins! Natural Blackjack!')
        tim.get_hand()
        jake.get_dealer_hand()
        tim.add_winnings(1)
        print(f'Current winnings: ${tim.get_winnings()}')
        play_game = input("Enter 'play' to keep playing blackjack.\n")
        continue
    hit_or_stand = input("Do you want to 'hit' or 'stand'\n")
    while hit_or_stand == 'hit':
        the_card = the_shoe.get_card_shoe()
        tim.hit(the_card)
        tim.get_hand()
        print("Dealer's card showing", jake.first_card())
        if tim.is_over_21():
            print('Dealer wins! Player went over 21!')
            tim.get_hand()
            jake.get_dealer_hand()
            tim.lose_winnings(1)
            game_over = True
            break
        hit_or_stand = input("Do you want to 'hit' or 'stand'\n")
    if game_over != True:
        jake.get_dealer_hand()
        while ((dealer_hand_value[0] <= 16) and (dealer_hand_value[1] <= 16)):
            a_card = the_shoe.get_card_shoe()
            jake.hit_dealer(a_card)
            dealer_hand_value = jake.get_dealer_hand_value()
            jake.get_dealer_hand()
            if jake.is_dealer_over_21():
                print('Player wins! Dealer went over 21!')
                tim.get_hand()
                jake.get_dealer_hand()
                tim.add_winnings(1)
                game_over = True
                break
        if game_over != True:
            if jake.is_dealer_hand_greater(tim.get_hand_value()):
                print('Dealer wins!')
                tim.get_hand()
                jake.get_dealer_hand()
                tim.lose_winnings(1)
            elif tim.is_hand_greater(jake.get_dealer_hand_value()):
                print('Player wins!')
                tim.get_hand()
                jake.get_dealer_hand()
                tim.add_winnings(1)
            else:
                print('Tie!')
                tim.get_hand()
                jake.get_dealer_hand()
    print(f'Current winnings: ${tim.get_winnings()}')
    play_game = input("Enter 'play' to keep playing blackjack.\n")
print(f'Your winnings: ${tim.get_winnings()}')

