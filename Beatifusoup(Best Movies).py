import requests
from bs4 import BeautifulSoup
url =("https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=SKAY3ZG8KQNG1VVWNDD7&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_3")

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
list = soup.find("tbody", {"class": "lister-list"}).find_all("tr",)
count = 1
for tr in list:
    title = tr.find("td", {"class": "titleColumn"}).find("a").text
    year = tr.find("td", {"class": "titleColumn"}).find("span").text.strip("()")
    rating =tr.find("td",{"class": "ratingColumn imdbRating"}).find("strong").text

    print(f"{count}- film: {title} yıl: {year} puan: {rating}")
    count +=1