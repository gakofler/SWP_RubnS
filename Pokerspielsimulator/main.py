import random
import matplotlib.pyplot as plt

# Define the number of runs (iterations) for the simulation
runs = 1000000


# Define a class to represent a card
class Card(object):
    def __init__(self, color, rank):
        # Initialize the card with a color and a rank
        self._color = color
        self._rank = rank

    def __repr__(self):
        # Define how the card is represented as a string for printing
        colors = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = [
            "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King", "Ace"
        ]
        # Map numeric values to their corresponding names
        color_name = colors[self._color]
        rank_name = ranks[self._rank]
        return f"{rank_name} of {color_name}"


# Function to draw five random cards from the deck
def draw_five_cards(deck):
    # Draw 5 random cards without duplicates
    five_cards = random.sample(deck, 5)
    print(five_cards)
    return five_cards


# Function to check if a hand is a Royal Flush
def is_royal_flush(five_cards):
    first_color = five_cards[0]._color
    # Check if all cards have the same color and are the top 5 ranks
    return all(card._color == first_color for card in five_cards) and \
        all(card._rank in {8, 9, 10, 11, 12} for card in five_cards)


# Function to check if a hand is a Straight Flush
def is_straight_flush(five_cards):
    first_color = five_cards[0]._color
    smallest_rank = min(card._rank for card in five_cards)
    # Check if all cards have the same color and form a sequence
    return all(card._color == first_color for card in five_cards) and \
        all(card._rank in [smallest_rank + i for i in range(5)] for card in five_cards)


# Function to check if a hand is Four of a Kind
def is_four_of_a_kind(five_cards):
    ranks = [card._rank for card in five_cards]
    # Check if any rank appears four times
    return any(ranks.count(rank) == 4 for rank in ranks)


# Function to check if a hand is a Full House
def is_full_house(five_cards):
    ranks = [card._rank for card in five_cards]
    # Check if there's a set of three cards of the same rank and a pair
    return any(ranks.count(rank) == 3 for rank in ranks) and \
        any(ranks.count(rank) == 2 for rank in ranks)


# Function to check if a hand is a Flush
def is_flush(five_cards):
    first_color = five_cards[0]._color
    # Check if all cards have the same color
    return all(card._color == first_color for card in five_cards)


# Function to check if a hand is a Straight
def is_straight(five_cards):
    ranks = [card._rank for card in five_cards]

    # A Straight must have 5 unique ranks
    if len(set(ranks)) != 5:
        return False

    smallest_rank = min(ranks)
    # Check if the ranks form a sequence
    return all(smallest_rank + i in ranks for i in range(5))


# Function to check if a hand is Three of a Kind
def is_three_of_a_kind(five_cards):
    ranks = [card._rank for card in five_cards]
    # Check if any rank appears three times
    return any(ranks.count(rank) == 3 for rank in ranks)


# Function to check if a hand is Two Pair
def is_two_pair(five_cards):
    ranks = [card._rank for card in five_cards]
    # Two Pair means there are at most 3 different ranks (2 pairs + 1 card)
    return len(set(ranks)) <= 3


# Function to check if a hand is One Pair
def is_pair(five_cards):
    ranks = [card._rank for card in five_cards]
    # One Pair means there are at most 4 different ranks
    return len(set(ranks)) <= 4


if __name__ == '__main__':
    # Create a deck with all possible card combinations (52 cards)
    deck = [Card(color, rank) for color in range(4) for rank in range(13)]

    # Dictionary to store counts of each poker hand ranking
    poker_hand_rankings = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Four of a Kind": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a Kind": 0,
        "Two Pair": 0,
        "One Pair": 0,
        "High Card": 0
    }

    # Run the simulation to draw hands and classify them
    for _ in range(runs):
        five_cards = draw_five_cards(deck)

        # Check for each hand ranking in order of priority
        if is_royal_flush(five_cards):
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
            # If no other hand ranking matches, it is a High Card
            poker_hand_rankings["High Card"] += 1

    # Print the results of the simulation
    print(poker_hand_rankings)

    # Create a bar chart to visualize the results
    hands = list(poker_hand_rankings.keys())
    counts = list(poker_hand_rankings.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(hands, counts, color='blue', align='center')
    plt.title('Poker Hand Rankings')
    plt.xlabel('Hand Type')
    plt.ylabel('Occurrences')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Display percentages above each bar
    for bar, count in zip(bars, counts):
        percentage = round(count / runs * 100, 2)  # Calculate and round the percentage
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f"{percentage}%", ha='center', va='bottom')  # Display the formatted percentage

    # Show the bar chart
    plt.show()
