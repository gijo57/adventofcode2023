with open('input.txt') as f:
    cards = f.read().split('\n')

result1 = 0
scratchcards = dict.fromkeys(range(1, len(cards) + 1), 1)

for i, card in enumerate(cards):
    card_index = i + 1
    parts = card.split('|')
    my_numbers = [int(num) for num in parts[1].split(' ') if num.isdigit()]
    winning_numbers = [int(num) for num in parts[0].split(' ') if num.isdigit()]
    card_points = 0
    matching_numbers = 0

    for num in my_numbers:
        if num in winning_numbers:
            matching_numbers += 1
            card_points = 1 if card_points == 0 else card_points * 2
    result1 += card_points

    for val in range(matching_numbers):
        card_number = val + card_index + 1
        scratchcards[card_number] += scratchcards[card_index]

result2 = sum(scratchcards.values())
print(result1, result2)