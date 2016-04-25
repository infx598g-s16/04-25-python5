# params should be a list of strings
def is_flush(cards):
    words = cards[0].split(' ')
    suit = words[2] #suit of the first guy

    for card in cards:
        print("Looking at "+card)
        if not card.endswith(suit):
            return False
    return True

result1 = is_flush(['5 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Clubs', '2 of Clubs'])
print(result1)

result2 = is_flush(['2 of Clubs', '9 of Clubs', '8 of Clubs', 'Jack of Spades', '2 of Clubs'])
print(result2)

is_flush(3)