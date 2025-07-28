import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

def get_games(target_date=None):
    if target_date is None:
        target_date = date.today()
    elif isinstance(target_date, str):
        target_date = date.fromisoformat(target_date)

    url = f"https://www.espn.com/mlb/schedule/_/date/{target_date.strftime('%Y%m%d')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    games = []
    rows = soup.select("table tbody tr")

    for row in rows:
        teams = row.select("td:nth-child(1)")
        if teams and " - " in teams[0].text:
            matchup = teams[0].text.split(" - ")
            games.append({"away": matchup[0].strip(), "home": matchup[1].strip()})

    return games

def get_next_3_days():
    all_games = []
    for i in range(3):
        day = date.today() + timedelta(days=i)
        day_games = get_games(day)
        for game in day_games:
            game['date'] = day.isoformat()
        all_games.extend(day_games)
    return all_games
