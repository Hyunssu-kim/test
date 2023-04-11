import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime

# 크롤링할 뉴스 기사의 검색어와 페이지 수를 설정합니다.
query = '크롤링'
pages = 3

# 뉴스 기사의 제목, 내용, 링크를 저장할 리스트를 생성합니다.
titles = []
contents = []
links = []

# 검색어와 페이지 수에 해당하는 뉴스 기사를 크롤링합니다.
for i in range(1, pages + 1):
    url = f'https://search.naver.com/search.naver?&where=news&query={query}&start={i*10-9}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_list = soup.select('.news_area')

    for news in news_list:
        title = news.select_one('.news_tit').text
        content = news.select_one('.news_dsc').text
        link = news.select_one('.news_tit')['href']
        titles.append(title)
        contents.append(content)
        links.append(link)

# 크롤링한 데이터를 Excel 파일에 저장합니다.
wb = openpyxl.Workbook()
ws = wb.active
ws.append(['제목', '내용', '링크'])

for title, content, link in zip(titles, contents, links):
    ws.append([title, content, link])

wb.save(datetime.datetime.now().strftime('%Y-%m-%d')+'_news.xlsx')