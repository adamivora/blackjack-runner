def should_hit(hand, dealer_card):
    """
    Strategy source: https://en.wikipedia.org/wiki/Blackjack#Basic_strategy
    """
    score = hand.get_score()
    aces = hand.aces
    dc = dealer_card.get_numeric_value()

    if aces == 0:
        if score >= 17:
            return False
        if score >= 13:
            return dc not in range(2, 7)
        if score == 12:
            return dc not in range(4, 7)
    else:
        if score >= 19:
            return False
        if score == 18:
            return dc not in range(2, 9)
    return True
