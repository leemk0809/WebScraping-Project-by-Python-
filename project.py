import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("「今日の天気」")
    url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    skyInfo = soup.find("p", attrs={"class":"pict"}).get_text().strip()

    highTemp = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"high"}).find("em").get_text()
    highTempGap = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"high"}).get_text()
    lowTemp = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"low"}).find("em").get_text()
    lowTempGap = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"low"}).get_text()

    highTempGap = highTempGap.replace("℃[","").replace("]","").replace(highTemp,"")
    lowTempGap = lowTempGap.replace("℃[","").replace("]","").replace(lowTemp,"")

    print(f"{skyInfo}、昨日より{highTempGap}℃ 高いです。")
if __name__ == "__main__":
    scrape_weather()