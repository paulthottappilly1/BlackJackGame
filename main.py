from art import logo
import random
import os

#function to clear the output from the terminal
def clear(): 
    os.system('cls' if os.name == 'nt' else 'clear')

#function to deal a card to the user or computer
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

#function to calculate the score
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#function to compare the user and computer scores to determine winner
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose\n"
    if user_score == computer_score:
        return "It's a draw\n"
    elif computer_score == 0:
        return "You lose! Computer got a blackjack!\n"
    elif user_score == 0:
        return "You win! You had a blackjack!\n"
    elif computer_score > 21:
        return "Computer went over. You win!\n"
    elif user_score > 21:
        return "You went over. You lose!\n"
    elif user_score > computer_score:
        return "You had a higher score, you win!\n"
    elif computer_score > user_score:
        return "The computer had a higher score, you lose!\n"

def playblackjack():

    print(logo)
    #variables for game functionality
    user_cards = []
    computer_cards = []
    game_over = False

    #for loop that gives both the user and computer two cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
    #creating a variable to hold the user's and computer's score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        #checks to see if the user or computer got blackjack or if the user's score went over 21
        #after that it prompts the user to draw another card or to stop drawing cards
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("Would you like to draw another card? Type 'y' for yes or 'n' to pass: ")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
        
        #the computer will keep drawing unless it has blackjack or has a score below 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    #displays the final totals for both user and computer and tells you who won
    print(f"Your final hand: {user_cards}, Final user score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Final computer score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  playblackjack()