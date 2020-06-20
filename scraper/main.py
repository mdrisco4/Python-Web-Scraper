from bs4 import BeautifulSoup
import requests

search = input("Search for: ")
params = {"q", search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
print(results.prettify())