from bs4 import BeautifulSoup
from urllib.request import urlopen as req

url = "http://stopcov.ge"
res = req(url)
html = res.read()
res.close()
bs4 = BeautifulSoup(html, "html.parser")
statsTable = bs4.find("div", class_="statistic-col")
statsItems = statsTable.find_all("li")
totalCases = statsItems[0].find_all("span", class_="quantity-numver")[0].text.rstrip()
lastCases = statsItems[0].find_all("span", class_="quantity-numver")[1].text.rstrip()
totalRecovered = statsItems[1].find_all("span", class_="quantity-numver")[0].text.rstrip()
lastRecovered = statsItems[1].find_all("span", class_="quantity-numver")[1].text.rstrip()
totalDeaths = statsItems[2].find_all("span", class_="quantity-numver")[0].text.rstrip()
lastDeaths = statsItems[2].find_all("span", class_="quantity-numver")[1].text.rstrip()
quarantine = statsItems[3].find_all("span", class_="quantity-numver")[0].text.rstrip()
hospitalize = statsItems[4].find_all("span", class_="quantity-numver")[0].text.rstrip()
covidHotels = statsItems[5].find_all("span", class_="quantity-numver")[0].text.rstrip()
text = f"total cases: {totalCases} (In last 24 hours {lastCases});\ntotal Recovered: {totalRecovered} (In last 24 hours {lastRecovered});\ntotal deaths: {totalDeaths} (In last 24 hours {lastDeaths});\nquarantined: {quarantine};\nHospitalized: {hospitalize};\nIn Covid hotels: {covidHotels}"
print(text)
