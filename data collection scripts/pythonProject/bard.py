import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/benson-hedges-world-series-cup-1979-80-60807/australia-vs-england-10th-match-65295/full-scorecard"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

batsmen = soup.find_all("tr", class_="ds-text-right")

for batsman in batsmen:
    name = batsman.find("a").text
    country = batsman.find("td", class_="ds-min-w-max")
    print(f"{name} from {country}")
