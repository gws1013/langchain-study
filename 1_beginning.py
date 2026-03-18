# 기초 사용법
OpenAI Platform 문서 참고: https://platform.openai.com/docs/quickstart?language=python

import os

os.environ["OPENAI_API_KEY"] = "sk-proj"

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.2",
    input="Agent가 뭔가요?"
)

print(response.output_text)

prompt = """
앵무새의 털 색상이 여러개인 이유가 뭐야?
"""

response = client.responses.create(
    model="gpt-5-nano",
    reasoning={"effort": "medium"},
    input=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.output_text)
