import openai as my_openai
import os
from dotenv import load_dotenv

load_dotenv()
client=my_openai.OpenAI(
    api_key=os.getenv("openai_key")
)
def ask_ai(question,content):
    response=client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system","content":content},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

my_prompt=input("Please give me your question\n")
my_response=ask_ai(my_prompt,"you are a assistant")
print(my_response)


