# 9.2 Poker hand
# A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts,
# or spades (denoted C, D, H, S). Each card also has a value of either 2 through 10, jack,
# queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A). For scoring purposes
# card values are ordered as above, with 2 having the lowest and ace the highest value. The
# suit has no impact on value.
# # A poker hand consists of five cards. Poker hands are ranked by the following partial
# order from lowest to highest.
#
# High Card
# Hands which do not fit any higher category are ranked by the value of their highest card.
#
# Pair
# Two of the five cards in the hand have the same value.
#
# Two Pairs
# The hand contains two different pairs.
#
# Three of a Kind
# Three of the cards in the hand have the same value.
#
# Straight
# Hand contains five cards with consecutive values.
#
# Flush
# Hand contains five cards of the same suit.
#
#
# Full House
# Three cards of the same value, with the remaining two cards forming a pair.
#
# Four of a Kind
# Four cards with the same value.
#
# Straight Flush
# Five cards of the same suit in numerical order.
#
# Royal Flush
# Consists of the ace, king, queen, jack and ten of a suit.
#
#
# Напишите программу, которая получает на вход пять карт и выводит старшую покерную
# комбинацию, которая образуется этими картами.
# Формат ввода:
# Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.
# Формат вывода:
# Название старшей комбинации, сформировавшейся на пришедшем наборе.
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# list of cards
hand = [i for i in input().split()]
suits = ""
cards = [""] * 5
result = ""
for i in range(5):
    suits += hand[i][-1]
    cards[i] = deck.index(hand[i][0:-1])
# sort card by value
cards.sort()
# suits all card is equal
if suits.count(suits[0]) == 5:
    if cards[0] == 8:
        result = "Royal Flush"  # Consists of the ace, king, queen, jack and ten of a suit
    elif cards[4] - cards[0] == 4:
        result = "Straight Flush"  # Five cards of the same suit in numerical order
    else:
        result = "Flush"  # Hand contains five cards of the same suit
else:  # more than one suit
    if cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4:
        result = "Four of a Kind"   # Four cards with the same value
    elif len(set(cards)) == 5 and cards[4] - cards[0] == 4:
        result = "Straight"  # Hand contains five cards with consecutive values
    elif cards.count(cards[0]) + cards.count(cards[4]) == 5:
        result = "Full House"  # Three cards of the same value, with the remaining two cards forming a pair
    else:
        result = "High Card"  # Hands which do not fit any higher category are ranked by the value of their highest card
        is_pair = False
        for i in range(5):
            if cards.count(cards[i]) == 3:
                result = "Three of a Kind"  # Three of the cards in the hand have the same value
                break
            if cards[i:].count(cards[i]) == 2:
                if is_pair:
                    result = "Two Pairs"  # The hand contains two different pairs
                    break
                else:
                    result = "Pair"  # Two of the five cards in the hand have the same value
                    is_pair = True
print(result)
