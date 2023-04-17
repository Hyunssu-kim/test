import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime
import instaUp
import openai

query = '산불'

url = f'https://search.naver.com/search.naver?&where=news&query={query}&start=1&sort=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.select('.news_area')

if len(articles) > 0:
    news = articles[0]
    title = news.select_one('.news_tit').text
    content = news.select_one('.news_dsc').text
    print(title)
    print(content)
else:
    print("해당 검색어의 기사를 찾을 수 없습니다.")

ws = str(title) + str(content)

openai.api_key = "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"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text
    return message.strip()

prompt = ws + ' 라는 내용을 해당 내용을 수능시험 형태로 새로운 문제를 만들어 그리고 답을 아래에 적어줘'
generated_text = generate_text(prompt)


print(generated_text  + "            에 대한 내용")
