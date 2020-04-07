from bs4 import BeautifulSoup
import requests

res = requests.get("http://stopcov.ge")
bs4 = BeautifulSoup(res.content, "html.parser")
data = list(filter(lambda x: x != '', bs4.find_all("div", class_="statistic-col")[0].text.split('\n')[:-2]))
cases = data[0].split("-")[1].strip()
recovered = data[1].split("-")[1].strip()
deaths = data[2].split("-")[1].strip()
quarantine = data[3].split("-")[1].strip()
active = data[4].split("-")[1].strip()
text = f"total cases: {cases}, recovered: {recovered}, deaths: {deaths}, quarantine: {quarantine}, active cases: {active}"
print(text)
