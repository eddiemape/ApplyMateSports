import requests
from bs4 import BeautifulSoup
from datetime import date

def get_games():
    url = f"https://www.espn.com/mlb/schedule/_/date/{date.today().strftime('%Y%m%d')}"
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
