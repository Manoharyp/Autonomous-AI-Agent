
import requests

def fetch_ai_headlines():
    API_KEY = "pub_78363dfcaec340aea4603c7e161afb7db0871"  # 🔁 Replace with your key
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q=artificial+intelligence&language=en"

    response = requests.get(url)
    data = response.json()

    headlines = []
    for article in data.get("results", [])[:5]:
        headlines.append(article["title"])

    return headlines
