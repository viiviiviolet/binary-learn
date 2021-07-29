# importing
import random
import time

# initialize variables
bank = 0
total = 0
dealer_total = 0
dealer_revealed_total = 0
hand = []
split_hand = []
dealer_hand = []
card = ""

# build deck
values = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}
deck = list(decklist)*4

def deal(deck):
    random.shuffle(deck)
    for i in range(2):
        card = deck.pop()
        hand.append(card)
        total += values[card]
    print(f'You were dealt a {hand[0]} and a {hand[1]}. Your current total is {total}')
    for i in range(2):
        card = deck.pop()
        dealer_hand.append(card)
        dealer_total += values[card]
    dealer_revealed_total += values[card]
    print(f'The dealer was dealt a face-down card and a {dealer_hand[1]}. Their current revealed total is {dealer_revealed_total}.')
    if dealer_hand[1] == "Ace":
        while True:
            insurance = input("Would you like to buy insurance? (y/n) ")
            if insurance == y:
                insurancebet = bet // 2
                pool -= insurancebet
                print(f'You bet {insurancebet} tokens for insurance.')
                if dealer_total == 21:
                    print(f'The Dealer had blackjack! You win the insurance bet. You have gained {bet} tokens')
                    pool += bet
                else:
                    print(f'The Dealer did not have blackjack. You have lost {insurancebet} tokens.')

def hit(hand, deck, total):
    card = deck.pop()
    hand.append(card)
    total += values[deck]

def reset():
    deck = list(decklist) * 4
    total = 0
    dealer_total = 0
    dealer_revealed_total = 0
    hand = []
    split_hand = []
    dealer_hand = []
    card = ""

def dealerturn():
    print(f'The dealer has revealed that their face-down card was a {dealer_hand[0]}. Their current total is {dealer_total}')
    if 'Ace' in dealer_hand and (values[dealer_hand[1]] == 10 or (values[dealer_hand[0]]) == 10):
        print("The dealer has Blackjack. You lost.")
    while dealer_total < 17:
        hit(dealer_hand, deck, dealer_total)
        print(f'The dealer drew a {card}. Their total is now {dealer_total}.')
    if dealer_total > 21:
        print(f'The dealer has bust. You win {bet*2} tokens.')
        bank += bet*2
    elif dealer_total > total:
        print(f'The dealer has won, you have lost your {bet} token bet.')
    elif dealer_total == total:
        print(f"It's a push. your {bet} token bet has been returned to the bank.")
    elif dealer_total < total:
        print(f'You win! You have won {bet*2} tokens')
        bank += bet*2

def split():
    # WIP

# main
while True:
    bank = 100
    print('You have been given 100 tokens to start with')
    while bank > 0:
        while True:
            bet = int(input('How many tokens would you like to bet? '))
            if bet > bank:
                print("You do not have enough tokens to bet that much")
            else:
                bank -= bet
                break
        print('Dealing...')
        time.sleep(1.0)
        deal(deck)
        while True:
            action = input(f"Your current total is {total}. Would you like to:\n1. Hit\n2. Stand\n3. Double Down\n4. Split")
            if action == '1':
                hit(hand, deck, total)
                print(f'You drew a {card}. Your total is now {total}.')
            elif action == '2':
                break
            elif action == '3':
                if len(hand) != 2:
                    print('You can only double down with only two cards.')
                else:
                    hit(hand, deck, total)
                    print(f'You doubled your bet and drew a {card}. Your final total is {total}.')
                    pool -= bet
                    bet *= 2
                    # WIP
                    break
            elif action == '4':
                if values[hand[0]] == values[hand[1]] or hand.len() > 2:
                    print("You can only split with doubles")
                else:
                    # WIP
            else:
                print("Please enter a valid input")
            if total > 21:
                print("You have busted")
                reset()
                break
        if total <= 21:
            print("It is now the dealer's turn")
            dealerturn()
            reset()
            while True:
                again = input('Would you like to continue playing? (y/n) ')
                if again == 'y':
                    break
                if again == 'n':
                    print("Goodbye.")
                    time.sleep(2)
                    quit()
            break
        else:
            reset()
            break




