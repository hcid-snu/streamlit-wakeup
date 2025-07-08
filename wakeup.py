import requests
from datetime import datetime

course = "dj2025"
team = ["team1", "team2", "team3", "team4", "team5", "team6"]
for t in team:
    url = f"https://{course}-{t}.streamlit.app/"
    res = requests.get(url)
    print(f"{course}-{t}: {datetime.now()}: {res.status_code} for {url}")
