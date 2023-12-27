from collections import Counter

with open('input.txt') as f:
    hands = [hand.strip().split(' ') for hand in f.readlines()]
    card_strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    card_strengths2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def rank_hand(hand, use_jokers):
    jokers = hand.count('J')
    card_count = Counter(hand)
    most_common_counts = [list(i) for i in card_count.most_common()]
    score = 0

    if use_jokers and jokers < 5:
        if most_common_counts[0][0] != 'J':
            most_common_counts[0][1] += jokers
        else:
            most_common_counts[1][1] += jokers
            most_common_counts = sorted(most_common_counts, reverse=True,key=lambda x: x[1])
        most_common_counts = [card_set for card_set in most_common_counts if card_set[0] != 'J']

    if most_common_counts[0][1] >= 5:
        score = 6
    elif most_common_counts[0][1] == 4:
        score = 5
    elif most_common_counts[0][1] == 3:
        if most_common_counts[1][1] == 2:
            score = 4
        else:
            score = 3
    elif most_common_counts[0][1] == 2:
        if most_common_counts[1][1] == 2:
            score = 2
        else:
            score = 1
    else:
        return score
    return score


hands1 = sorted(hands, key=lambda hand: (rank_hand(hand[0], False), [card_strengths.index(card) for card in hand[0]]))
hands2 = sorted(hands, key=lambda hand: (rank_hand(hand[0], True), [card_strengths2.index(card) for card in hand[0]]))

result1 = 0
for i, hand in enumerate(hands1):
    rank = i + 1
    result1 += int(hand[1]) * rank

result2 = 0
for i, hand in enumerate(hands2):
    rank = i + 1
    result2 += int(hand[1]) * rank

print(result1, result2)
