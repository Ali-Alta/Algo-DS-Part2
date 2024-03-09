def playing_domino(cards, deck):
    for card in cards:
        if card[0] == deck[0]:
            deck.insert(0, card[0])
            cards.remove(card)
            return deck
        elif card[0] == deck[0]:
            deck.insert(0, card[0])
            cards.remove(card)
            return deck
        elif card[0] == deck[-1]:
            deck.append(card[1])
            cards.remove(card)
            return deck
        elif card[0] == deck[-1]:
            deck.append(card[0])
            cards.remove(card)
            return deck
    return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []
