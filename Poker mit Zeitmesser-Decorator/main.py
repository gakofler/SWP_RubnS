import functools
import random
import time
import matplotlib.pyplot as plt

# Zeitmesser-Decorator
def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} dauerte {end_time - start_time:.6f} Sekunden")
        return result
    return wrapper

# Define a class to represent a card
class Card(object):
    def __init__(self, color, rank):
        self._color = color
        self._rank = rank

    def __repr__(self):
        colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        color_name = colors[self._color]
        rank_name = ranks[self._rank]
        return f"{rank_name} of {color_name}"

def draw_cards(deck, num_cards):
    return random.sample(deck, num_cards)

def is_royal_flush(five_cards, max_rank):
    first_color = five_cards[0]._color
    return all(card._color == first_color for card in five_cards) and \
        all(card._rank in [rank for rank in range(max_rank+1-len(five_cards), max_rank+1)] for card in five_cards)

def is_straight_flush(five_cards):
    first_color = five_cards[0]._color
    smallest_rank = min(card._rank for card in five_cards)
    return all(card._color == first_color for card in five_cards) and \
        all(card._rank in [smallest_rank + i for i in range(5)] for card in five_cards)

def is_four_of_a_kind(five_cards):
    ranks = [card._rank for card in five_cards]
    return any(ranks.count(rank) == 4 for rank in ranks)

def is_full_house(five_cards):
    ranks = [card._rank for card in five_cards]
    return any(ranks.count(rank) == 3 for rank in ranks) and \
        any(ranks.count(rank) == 2 for rank in ranks)

def is_flush(five_cards):
    first_color = five_cards[0]._color
    return all(card._color == first_color for card in five_cards)

def is_straight(five_cards):
    ranks = [card._rank for card in five_cards]
    if len(set(ranks)) != 5:
        return False
    smallest_rank = min(ranks)
    return all(smallest_rank + i in ranks for i in range(5))

def is_three_of_a_kind(five_cards):
    ranks = [card._rank for card in five_cards]
    return any(ranks.count(rank) == 3 for rank in ranks)

def is_two_pair(five_cards):
    ranks = [card._rank for card in five_cards]
    return len(set(ranks)) <= 3

def is_pair(five_cards):
    ranks = [card._rank for card in five_cards]
    return len(set(ranks)) <= 4

@time_it
def run_simulation(runs, deck, max_rank):
    poker_hand_rankings = {"Royal Flush": 0, "Straight Flush": 0, "Four of a Kind": 0, "Full House": 0,
                           "Flush": 0, "Straight": 0, "Three of a Kind": 0, "Two Pair": 0, "One Pair": 0, "High Card": 0}
    for _ in range(runs):
        five_cards = draw_cards(deck, 5)
        if is_royal_flush(five_cards, max_rank):
            poker_hand_rankings["Royal Flush"] += 1
        elif is_straight_flush(five_cards):
            poker_hand_rankings["Straight Flush"] += 1
        elif is_four_of_a_kind(five_cards):
            poker_hand_rankings["Four of a Kind"] += 1
        elif is_full_house(five_cards):
            poker_hand_rankings["Full House"] += 1
        elif is_flush(five_cards):
            poker_hand_rankings["Flush"] += 1
        elif is_straight(five_cards):
            poker_hand_rankings["Straight"] += 1
        elif is_three_of_a_kind(five_cards):
            poker_hand_rankings["Three of a Kind"] += 1
        elif is_two_pair(five_cards):
            poker_hand_rankings["Two Pair"] += 1
        elif is_pair(five_cards):
            poker_hand_rankings["One Pair"] += 1
        else:
            poker_hand_rankings["High Card"] += 1
    return poker_hand_rankings

if __name__ == '__main__':
    deck = [Card(color, rank) for color in range(4) for rank in range(13)]
    max_rank = max(card._rank for card in deck)
    runs = int(input("How many runs would you like to simulate? "))
    results = run_simulation(runs, deck, max_rank)
    print(results)
