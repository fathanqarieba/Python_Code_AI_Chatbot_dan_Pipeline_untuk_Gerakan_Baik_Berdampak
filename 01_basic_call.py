import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
SUMOPOD_BASE_URL= os.getenv("SUMOPOD_BASE_URL")
SUMOPOD_API_KEY= os.getenv("SUMOPOD_API_KEY")

client = OpenAI(base_url=SUMOPOD_BASE_URL,api_key=SUMOPOD_API_KEY)

#completion -> https://ai.sumopod.com/v1/chat/completions -> llm inference -> stateless (diat tiadak menyimpan apapun untuk nex requestnya)
completion = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[{"role":"user", "content":"hallo, jelasin aku soal hidup"}])

# messages = list [messages]
# role -> system, user, assistant, lainnya( developer, tools)
# content -> string content
final_output = completion.choices[0].message.content
usage = completion.usage
assert usage is not None
print(final_output)
print(usage.prompt_tokens)
print(usage.completion_tokens)
print(usage.total_tokens)
#harness realibility vs model capability, sebagus apapun aplikasi (harness), modelnya ngaruh ke performa


