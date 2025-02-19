import random
from art import logo

# Function to calculate the total score of a hand
# Converts Ace (11) to 1 if needed to prevent busting

def calculate_score(cards):
    score = sum(cards)
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

# Function to randomly choose a card from the deck
def card_chooser():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Main function to play the game
def blackjack():
    print(logo)
    user_cards = [card_chooser(), card_chooser()]
    computer_cards = [card_chooser()]

    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your current hand : {user_cards}. Total score : {user_score}")
        print(f"Computer's First Card : {computer_cards}")

        # Check for BlackJack or bust condition
        if user_score == 21:
            print("BlackJack! You win!")
            return
        elif user_score > 21:
            print("You went over! You lose!")
            return

        ans = input("Do you want to pick another card? : \n'y' --> yes\n'n' --> no")
        if ans.lower() == "y":
            user_cards.append(card_chooser())
        else:
            break

    # Dealer's turn
    while computer_score < 17:
        computer_cards.append(card_chooser())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, Total sum : {user_score}.")
    print(f"Computer's final hand : {computer_cards}, Total sum : {computer_score}")

    # Determine the winner
    if computer_score > 21 or user_score > computer_score:
        print("You Win!")
    elif computer_score == user_score:
        print("It's a draw!")
    else:
        print("You lose!")

    continuation = input("Do you want to continue? : \n'y' --> yes\n'n' --> no")
    if continuation.lower() == 'y':
        print("\n" * 25)
        blackjack()

if input("Do you want to play a game of Blackjack? (y/n): ").lower() == 'y':
    blackjack()
