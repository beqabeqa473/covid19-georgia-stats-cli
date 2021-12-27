from bs4 import BeautifulSoup
from urllib.request import urlopen as req


class CovidParser():

    SITE_URL = "http://stopcov.ge"

    def parse(self):
        res = req(self.SITE_URL)
        html = res.read()
        res.close()
        bs4 = BeautifulSoup(html, "html.parser")
        statsTable = bs4.find("div", class_="statistic-col")
        statsItems = statsTable.find_all("li")
        self.totalCases = statsItems[0].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.lastCases = statsItems[0].find_all("span", class_="quantity-numver")[1].text.rstrip()
        self.totalRecovered = statsItems[1].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.lastRecovered = statsItems[1].find_all("span", class_="quantity-numver")[1].text.rstrip()
        self.totalDeaths = statsItems[2].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.lastDeaths = statsItems[2].find_all("span", class_="quantity-numver")[1].text.rstrip()
        self.lastTests = statsItems[3].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.antigenTests = statsItems[3].find_all("span", class_="quantity-numver")[1].text.rstrip()
        self.pcrTests = statsItems[3].find_all("span", class_="quantity-numver")[2].text.rstrip()
        positiveCases = statsItems[4].text.split(":")[1].split(", ")
        self.positiveCasesPerDay = positiveCases[0].split("-")[1].strip()
        self.positiveCasesPerTwoWeeks = positiveCases[1].split("-")[1].strip()
        self.positiveCasesPerWeek = positiveCases[2].split("-")[1].strip()
        self.totalVaccined = statsItems[5].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.lastVaccined = statsItems[5].find_all("span", class_="quantity-numver")[1].text.rstrip()
        self.quarantine = statsItems[6].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.hospitalize = statsItems[7].find_all("span", class_="quantity-numver")[0].text.rstrip()
        self.clinicHotels = statsItems[8].find_all("span", class_="quantity-numver")[0].text.rstrip()
