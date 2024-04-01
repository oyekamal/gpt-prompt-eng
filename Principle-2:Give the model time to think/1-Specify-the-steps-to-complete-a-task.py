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
text = f"""
In a charming village, siblings Jack and Jill set out on \ 
a quest to fetch water from a hilltop \ 
well. As they climbed, singing joyfully, misfortune \ 
struck—Jack tripped on a stone and tumbled \ 
down the hill, with Jill following suit. \ 
Though slightly battered, the pair returned home to \ 
comforting embraces. Despite the mishap, \ 
their adventurous spirits remained undimmed, and they \ 
continued exploring with delight.
"""
# example 1
prompt_1 = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple \
backticks with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following \
keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
```{text}```
"""
response = get_completion(prompt_1)
print("Completion for prompt 1:")
print(response.content)


#output
# 1 - Jack and Jill, siblings on a quest for water, face misfortune but remain adventurous.

# 2 - Jack et Jill, frère et sœur en quête d'eau, font face à la malchance mais restent aventureux.

# 3 - Jack, Jill

# 4 - 
# {
#   "french_summary": "Jack et Jill, frère et sœur en quête d'eau, font face à la malchance mais restent aventureux.",
#   "num_names": 2
# }


prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by 
  <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the 
  following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>
"""
response = get_completion(prompt_2)
print("\nCompletion for prompt 2:")
print(response.content)
#output 

# Summary: Jack and Jill, siblings, go on a quest to fetch water but encounter misfortune on the way back.

# Translation: Jack et Jill, frère et sœur, partent en quête d'eau mais rencontrent des malheurs sur le chemin.

# Names: Jack, Jill

# Output JSON: 
# {
#   "french_summary": "Jack et Jill, frère et sœur, partent en quête d'eau mais rencontrent des malheurs sur le chemin.",
#   "num_names": 2
# }