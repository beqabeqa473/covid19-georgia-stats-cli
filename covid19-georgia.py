from bs4 import BeautifulSoup
import re
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
lastTests = statsItems[3].find_all("span", class_="quantity-numver")[0].text.rstrip()
antigenTests = statsItems[3].find_all("span", class_="quantity-numver")[1].text.rstrip()
pcrTests = statsItems[3].find_all("span", class_="quantity-numver")[2].text.rstrip()
positiveCasesPerDay, positiveCasesPerTwoWeeks, positiveCasesPerWeek = re.findall("\d+,\d+%", statsItems[4].text)
totalVaccined = statsItems[5].find_all("span", class_="quantity-numver")[0].text.rstrip()
lastVaccined = statsItems[5].find_all("span", class_="quantity-numver")[1].text.rstrip()
quarantine = statsItems[6].find_all("span", class_="quantity-numver")[0].text.rstrip()
hospitalize = statsItems[7].find_all("span", class_="quantity-numver")[0].text.rstrip()
clinicHotels = statsItems[8].find_all("span", class_="quantity-numver")[0].text.rstrip()
text = f"total cases: {totalCases} (In last 24 hours {lastCases});\ntotal Recovered: {totalRecovered} (In last 24 hours {lastRecovered});\ntotal deaths: {totalDeaths} (In last 24 hours {lastDeaths});\nTested in last 24 hours: {lastTests}, with Antigen tests: {antigenTests}, with PCR tests: {pcrTests};\nPositive cases: (per day - {positiveCasesPerDay}, per 7 days - {positiveCasesPerWeek}, per 14 days - {positiveCasesPerTwoWeeks});\nVaccined: (total - {totalVaccined}, last day - {lastVaccined});\nquarantined: {quarantine};\nHospitalized: {hospitalize};\nIn Clinic hotels: {clinicHotels}"
print(text)
