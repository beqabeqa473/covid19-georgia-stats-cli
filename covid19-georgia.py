#from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup

#session = HTMLSession()
#res = session.get("http://stopcov.ge")
res = requests.get("http://stopcov.ge")
bs4 = BeautifulSoup(res.content, "html.parser")
#data = bs4.find_all("div", class_="statistic-col")[0]
#filterObject = filter(lambda x: x != "", data)
#data_list = list(filterObject)
#data = bs4.find_all("div", class_="statistic-col")
#data = bs4.find_all("div", class_="statistic-col")[0].text.split('\n')[:-2]
#filterObject = list(filter(lambda x: x != '', data))
data = list(filter(lambda x: x != '', bs4.find_all("div", class_="statistic-col")[0].text.split('\n')[:-2]))
#html_table = res.html.find('.statistic-col', first=True)
#data = html_table.text.split('\n')[:-1]
cases = data[0].split("-")[1].strip()
recovered = data[1].split("-")[1].strip()
deaths = data[2].split("-")[1].strip()
quarantine = data[3].split("-")[1].strip()
active = data[4].split("-")[1].strip()
finalString = f"total cases: {cases}, recovered: {recovered}, deaths: {deaths}, quarantine: {quarantine}, active cases: {active}"
print(finalString)