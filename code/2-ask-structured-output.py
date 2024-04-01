from openai import OpenAI

import os 
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message


# prompt
prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
response = get_completion(prompt)
print(response.content)

# output 
# '[\n    {\n        "book_id": 1,\n        "title": "The Midnight Garden",\n        "author": "Elena Nightingale",\n        "genre": "Fantasy"\n    },\n    {\n        "book_id": 2,\n        "title": "Echoes of Eternity",\n        "author": "Lucas Starlight",\n        "genre": "Science Fiction"\n    },\n    {\n        "book_id": 3,\n        "title": "Whispers in the Wind",\n        "author": "Aria Moonshadow",\n        "genre": "Mystery"\n    }\n]'

