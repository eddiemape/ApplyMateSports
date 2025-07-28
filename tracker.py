def record_results(predictions):
    with open("results_log.txt", "a") as file:
        for game in predictions:
            file.write(f"{game['matchup']}: {game['winner']} ({game['confidence']}%)\n")
