import openai

openai.api_key = "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"

# 예시로 'Hello, world!' 문장 생성
prompt = "Hello, world!"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.7,
)
print(response.choices[0].text.strip())