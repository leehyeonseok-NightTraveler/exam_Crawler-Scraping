# pip install beautifulsoup4
import csv
import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename="네이버 코스피_시가총액 1-50위.csv"
# f = open(filename, "w", encoding="utf-8")
# encoding="utf-8-sig"
# f = open(filename, "w", encoding="utf-8-sig")
f = open(filename, "w", encoding="utf-8-sig" ,newline='') 
writer = csv.writer(f)

title = "N 종목명 현재가 전일비 등락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER ROE".split("\t")
writer.writerow(title)

#for page in range(1,3)
for page in range(1,2):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    date_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in date_rows:
        columns = row.find_all("td")
        # print("@# len=>", len(columns))
        if len(columns) == 1:
            continue
        # data = [column.get_text() for column in columns]
        data = [column.get_text().strip() for column in columns]
        # print(data)

        writer.writerow(data)

