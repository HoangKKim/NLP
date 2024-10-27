import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

open_api_key = os.getenv("OPEN_API_KEY")

# print(open_api_key)

client = OpenAI(
    # This is the default and can be omitted
    api_key= open_api_key
)

path = "./chatbot_project/text.txt"
with open(path, 'r', encoding= 'utf-8') as f:
    raw_text =  f.read()

# raw_text = "John Doe từ công ty ABC đã tham gia vào hội thảo khoa học ngày 12 tháng 10 năm 2023 tại New York."

response = client.chat.completions.create(
    messages=[
    {
        "role": "system",
        "content": """You are a data extraction assistant. 
                    Extract the following fields from the raw text: name, price, sales promotion, category, brand.
                    If the information were important but not in those fields, put them in 'extra' field. 
                    Return the result in JSON format."""
    },
    {
        "role": "user",
        "content": raw_text
    }
    ],
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=100
)

text_content = response.choices[0].message.content

print(text_content)