import openai as my_openai
import os
from dotenv import load_dotenv

load_dotenv()
my_openai.apikey=os.getenv("openai_key")
def ask_ai(question,content):
    response=my_openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system","content":content},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

my_prompt=input("Please give me your question")
my_response=ask_ai(my_prompt,"you are a assistant")


