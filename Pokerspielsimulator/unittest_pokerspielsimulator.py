import unittest
from main import Card, draw_cards, is_royal_flush, is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pair, is_pair


class TestPokerHandMethods(unittest.TestCase):
    def setUp(self):
        # Set up a deck and some common test cases
        self.deck = [Card(color, rank) for color in range(4) for rank in range(13)]
        self.royal_flush_hand = [
            Card(0, 8), Card(0, 9), Card(0, 10), Card(0, 11), Card(0, 12)
        ]  # Hearts: 10, J, Q, K, A
        self.straight_flush_hand = [
            Card(1, 4), Card(1, 5), Card(1, 6), Card(1, 7), Card(1, 8)
        ]  # Diamonds: 5, 6, 7, 8, 9
        self.four_of_a_kind_hand = [
            Card(0, 5), Card(1, 5), Card(2, 5), Card(3, 5), Card(0, 2)
        ]
        self.full_house_hand = [
            Card(0, 6), Card(1, 6), Card(2, 6), Card(0, 4), Card(1, 4)
        ]
        self.flush_hand = [
            Card(2, 1), Card(2, 4), Card(2, 6), Card(2, 9), Card(2, 12)
        ]
        self.straight_hand = [
            Card(0, 4), Card(1, 5), Card(2, 6), Card(3, 7), Card(0, 8)
        ]
        self.three_of_a_kind_hand = [
            Card(0, 7), Card(1, 7), Card(2, 7), Card(0, 3), Card(1, 9)
        ]
        self.two_pair_hand = [
            Card(0, 8), Card(1, 8), Card(0, 9), Card(1, 9), Card(0, 2)
        ]
        self.one_pair_hand = [
            Card(0, 10), Card(1, 10), Card(0, 3), Card(1, 4), Card(2, 6)
        ]
        self.high_card_hand = [
            Card(0, 1), Card(1, 3), Card(2, 6), Card(3, 8), Card(0, 10)
        ]

    def test_draw_cards(self):
        hand = draw_cards(self.deck, 5)
        self.assertEqual(len(hand), 5)
        self.assertTrue(all(card in self.deck for card in hand))
        self.assertEqual(len(set(hand)), 5)  # All cards must be unique

    def test_is_royal_flush(self):
        max_rank = max(card._rank for card in self.deck)
        self.assertTrue(is_royal_flush(self.royal_flush_hand, max_rank))
        self.assertFalse(is_royal_flush(self.flush_hand, max_rank))

    def test_is_straight_flush(self):
        self.assertTrue(is_straight_flush(self.straight_flush_hand))
        self.assertFalse(is_straight_flush(self.flush_hand))

    def test_is_four_of_a_kind(self):
        self.assertTrue(is_four_of_a_kind(self.four_of_a_kind_hand))
        self.assertFalse(is_four_of_a_kind(self.full_house_hand))

    def test_is_full_house(self):
        self.assertTrue(is_full_house(self.full_house_hand))
        self.assertFalse(is_full_house(self.three_of_a_kind_hand))

    def test_is_flush(self):
        self.assertTrue(is_flush(self.flush_hand))
        self.assertFalse(is_flush(self.straight_hand))

    def test_is_straight(self):
        self.assertTrue(is_straight(self.straight_hand))
        self.assertFalse(is_straight(self.flush_hand))

    def test_is_three_of_a_kind(self):
        self.assertTrue(is_three_of_a_kind(self.three_of_a_kind_hand))
        self.assertFalse(is_three_of_a_kind(self.two_pair_hand))

    def test_is_two_pair(self):
        self.assertTrue(is_two_pair(self.two_pair_hand))
        self.assertFalse(is_two_pair(self.one_pair_hand))

    def test_is_pair(self):
        self.assertTrue(is_pair(self.one_pair_hand))
        self.assertFalse(is_pair(self.high_card_hand))

    def test_card_representation(self):
        card = Card(0, 12)  # Ace of Hearts
        self.assertEqual(repr(card), "Ace of Hearts")

if __name__ == '__main__':
    unittest.main()