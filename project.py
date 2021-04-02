import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("「今日の天気」")
    url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    cast = soup.find("p", attrs={"class":"pict"}).get_text().strip()

    highTemp = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"high"}).find("em").get_text()
    highTempGap = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"high"}).get_text()
    lowTemp = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"low"}).find("em").get_text()
    #lowTempGap = soup.find("ul", attrs={"class":"temp"}).find("li", attrs={"class":"low"}).get_text()

    highTempGap = highTempGap.replace("℃[","").replace("]","").replace(highTemp,"")
    #lowTempGap = lowTempGap.replace("℃[","").replace("]","").replace(lowTemp,"")

    if int(highTempGap) > 0 :
        print(f"{cast}、昨日より{highTempGap}℃ 高いです。")
    else :
        print(f"{cast}、昨日より{highTempGap}℃ 低いです。")
    print(f"最低気温 {lowTemp}℃  / 最高気温 {highTemp}℃")

    rain_rates = soup.find("tr", attrs={"class":"precip"}).find_all("td")

    #print(morning_rain_rate)
    for idx, rain_rate in enumerate(rain_rates):
        if idx == 1:
            morning_rain_rate = rain_rate.get_text()
            if(morning_rain_rate == "---"):
                morning_rain_rate = "0%"
        elif idx == 2:
            afternoon_rain_rate = rain_rate.get_text()
            if(afternoon_rain_rate == "---"):
                afternoon_rain_rate = "0%"

    print(f"午前の放水確率 {morning_rain_rate} / 午後の放水確率 {afternoon_rain_rate}")
    print("\n")

def headline_news():
    print("「ヘッドラインニュース」")
    url = "https://news.yahoo.co.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    headlines = soup.find_all("a", attrs={"class":"sc-kIPQKe eMCmdt"})
    
    for idx, headline in enumerate(headlines):
        print(f"{idx+1}. {headline.get_text()}")
        print(f"リンク： {headline['href']}")
        if idx > 1 :
            break
    print("\n")

def it_news():
    print("「アイディニュース」")
    url = "https://news.yahoo.co.jp/categories/it"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    article = soup.find_all("a", attrs={"class":"sc-kIPQKe eMCmdt"})
    
    for idx, news in enumerate(article):
        print(f"{idx+1}. {news.get_text()}")
        print(f"リンク： {news['href']}")
        if idx > 1 :
            break
    print("\n")

def japanese_today():
    print("「今日の日本語」")
    url = "https://learn.dict.naver.com/jpdic/today/conversation.nhn"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    title_jp = soup.find("div", attrs={"class":"jp_tit jp"}).get_text()
    title_kr = soup.find("div", attrs={"class":"kr_tit"}).get_text()
    
    print("・文")
    print("-",title_jp)
    print("-",title_kr)
    print("-"*100)

    article_jp = soup.find("ul", attrs={"id":"todayConversation"})
    articles_jp = article_jp.find_all("li")

    for article in articles_jp:
        if article.find("span", attrs={"class":"ico_lfta notts"}):
            print(article.find("span", attrs={"class":"ico_lfta notts"}).get_text(),":",
                article["data-ttsurl"]
            )
        elif article.find("span", attrs={"class":"ico_lftb notts"}):
            print(article.find("span", attrs={"class":"ico_lftb notts"}).get_text(),":",
                article["data-ttsurl"]
            )
    print("-"*100)

    articles_kr = soup.find("ul", attrs={"class":"conv_lst conv_lst_v2"}).find_all("li")
    
    for article in articles_kr:
        speacker = article.get_text().strip()[0:1]
        text = article.get_text().strip()[1:]
        print(speacker, ":", text)
    print("-"*100)

if __name__ == "__main__":
    scrape_weather()
    headline_news()
    it_news()
    japanese_today()