from dotenv import load_dotenv

load_dotenv()
import os
import openai

# make sure your OPENAI_API_KEY is set

# call the openai ChatCompletion endpoint, with the ChatGPT model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, world!"},
    ]
)

# extract the response
print(response["choices"][0]["message"]["content"])
