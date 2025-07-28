from scraper import get_games
from stats import analyze_matchup

def get_daily_predictions():
    games = get_games()
    predictions = []

    for game in games:
        winner, confidence = analyze_matchup(game)
        predictions.append({
            "matchup": f"{game['away']} @ {game['home']}",
            "winner": winner,
            "confidence": confidence
        })

    return predictions
