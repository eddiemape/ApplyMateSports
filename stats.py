def analyze_matchup(game):
    # Placeholder - Replace with real stat comparison logic
    import random
    confidence = random.randint(60, 90)
    winner = game['home'] if confidence > 75 else game['away']
    return winner, confidence
