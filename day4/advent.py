with open('input.txt') as f:
    cards = f.read().split('\n')

    result1 = 0
    for card in cards:
        parts = card.split('|')
        my_numbers = [int(num) for num in parts[1].split(' ') if num.isdigit()]
        winning_numbers = [int(num) for num in parts[0].split(' ') if num.isdigit()]
        card_points = 0

        for num in my_numbers:
            if num in winning_numbers:
                card_points = 1 if card_points == 0 else card_points * 2
        result1 += card_points
    print(result1)