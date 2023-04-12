import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime

# 크롤링할 뉴스 기사의 검색어와 페이지 수를 설정합니다.
print(" * 마지막에 오른쪽 방향키 후 엔터  * 페이지는 숫자 아니면 오류나요~ ")
print(" 최신 기사 기준 검색어 입니다!")
print(" 문의 e-mail : foxkim951@naver.com ")
while 1 :
    print("!CTRL+C로빠져나오세요!")
    query = input("단어 입력 : ")
    pages = int(input("페이지 입력 : "))
    print("검색 시 [ 0 : view ] [ 1 : news ] ")
    where = int(input(" 검색 방향 검색 : "))
    print("검색 시 [ 0 : 관련도 ] [ 1 : 최신순 ] ")
    sort = int(input("옵션 : "))

    # 뉴스 기사의 제목, 내용, 링크를 저장할 리스트를 생성합니다.
    titles = []
    contents = []
    links = []

    # 검색어와 페이지 수에 해당하는 뉴스 기사를 크롤링합니다.
    for i in range(1, pages + 1):
        url = f'https://search.naver.com/search.naver?&where={where}&query={query}&start={i*10-9}&sort={sort}'
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

    wb.save(where+" "+query+"_"+datetime.datetime.now().strftime('%Y-%m-%d')+'_news.xlsx')
    print("생성 완료")
    print("end")
