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

user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
] 

for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Original message ({lang}): {issue}")

    prompt = f"""
    Translate the following  text to English \
    and Korean: ```{issue}```
    """
    response = get_completion(prompt)
    print(response.content, "\n")
    
    
#output

# Original message (ChatCompletionMessage(content='This is French.', role='assistant', function_call=None, tool_calls=None)): La performance du système est plus lente que d'habitude.
# English: "The system performance is slower than usual."

# Korean: "시스템 성능이 평소보다 느립니다." 

# Original message (ChatCompletionMessage(content='This is Spanish.', role='assistant', function_call=None, tool_calls=None)): Mi monitor tiene píxeles que no se iluminan.
# English: "My monitor has pixels that do not light up."

# Korean: "내 모니터에는 빛나지 않는 픽셀이 있습니다." 

# Original message (ChatCompletionMessage(content='Italian', role='assistant', function_call=None, tool_calls=None)): Il mio mouse non funziona
# English: My mouse is not working
# Korean: 내 마우스가 작동하지 않습니다 

# Original message (ChatCompletionMessage(content='This is Polish.', role='assistant', function_call=None, tool_calls=None)): Mój klawisz Ctrl jest zepsuty
# English: My Ctrl key is broken
# Korean: 제 Ctrl 키가 고장 났어요 

# Original message (ChatCompletionMessage(content='This is Chinese.', role='assistant', function_call=None, tool_calls=None)): 我的屏幕在闪烁
# English: My screen is flickering
# Korean: 내 화면이 깜박거립니다 