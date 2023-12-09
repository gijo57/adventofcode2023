from collections import Counter

with open('input.txt') as f:
    hands = [hand.strip().split(' ') for hand in f.readlines()]
    card_strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    card_strengths2 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A', 'J']


def rank_hand(hand, use_jokers):
    jokers = hand.count('J')
    has_joker = jokers > 0
    card_count = Counter(hand)
    most_common_counts = [list(i) for i in card_count.most_common()]
    score = 0

    if use_jokers and jokers < 5:
        most_common_counts[0][1] += jokers

    print(hand, most_common_counts)
    if most_common_counts[0][1] >= 5:
        score = 6 if jokers < 5 else 5 - jokers / 10
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
print(hands2)
result1 = 0
for i, hand in enumerate(hands1):
    rank = i + 1
    result1 += int(hand[1]) * rank

result2 = 0
for i, hand in enumerate(hands2):
    rank = i + 1
    result2 += int(hand[1]) * rank

print(result1, result2)
