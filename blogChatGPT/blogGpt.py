import openai
import re
import os
from datetime import datetime, timedelta

#openAi Api 키
openai.api_key = "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"

#주제 선정
city = "리그 오브 레전드"
topic = f" {city} 플레이 할 때 지켜야 할 사항"
category = "game"
print(topic)

# 프롬프트 (내용 수정 가능)
prompt = f'''
리그 오브 레전드를 플레이 할 때 지켜야 할 수칙들을 적어줘
'''

def generate_blog(topic, prompt):
    # 모델 엔진 선택
    model_engine = "text-davinci-003"

    # 맥스 토큰
    max_tokens = 2048

    # 블로그 생성
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.3,      # creativity
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion

response = generate_blog(topic, prompt)

# 생성된 글 출력
print(response.choices[0].text)

#해시태그 추출
hashtag_pattern = r'(#+[a-zA-Z0-9(_)]{1,})'

re.findall(hashtag_pattern, response['choices'][0]['text'])
#문자열변경
hashtags = [w[1:] for w in re.findall(hashtag_pattern, response['choices'][0]['text'])]
tag_string = ""
for w in hashtags:
    # 3글자 이상 추출
    if len(w) > 3:
        tag_string += f'{w}, '
tag_string

tag_string = re.sub(r'[^a-zA-Z, ]', '', tag_string)
tag_string = tag_string.strip()[:-1]
tag_string

#블로그 헤더
page_head = f'''---
layout: single
title:  "{topic}"
categories: {category}
tag: [{tag_string}]
toc: false
author_profile: false
sidebar:
    nav: "counts"
---
'''
print(page_head)

# 첫 줄은 타이틀(제목)과 겹치기 때문에 제거하도록 합니다.
body = '\n'.join(response['choices'][0]['text'].strip().split('\n')[1:])

output = page_head + body
print(output)

# 어제 일자 생성
yesterday = datetime.now() - timedelta(days=1)
yesterday

timestring = yesterday.strftime('%Y-%m-%d')
timestring

filename = f"{timestring}-{'-'.join(topic.lower().split())}.md"
filename

