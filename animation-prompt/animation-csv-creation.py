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

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message
  
# prompt
# given the sentiment from the lesson on "inferring",
# and the original customer message, customize the email
example_data = f"""character,emotion,intensity,head_direction,eyes_direction,screen_mode,body_action,reaction_bool,word,init,final,room,
5,1,1,3,2,4,18,FALSE,hi,0.57,0.8,0,0.23
5,1,1,3,2,4,18,FALSE,guys,0.8,1.27,0,0.47
5,1,2,3,2,4,4,FALSE,I'm,1.33,1.66,0,0.33
5,1,2,3,2,4,4,FALSE,kamal,1.66,2.14,1.5,0.48
5,1,2,3,2,4,4,FALSE,and,2.2,2.42,1.5,0.22
5,1,2,3,2,4,4,FALSE,I,2.46,2.7,1.5,0.24
5,1,1,3,2,4,4,FALSE,love,2.7,3.02,1.5,0.32
5,1,1,3,2,4,4,FALSE,auto mation,3.05,3.82,1.5,0.77
5,6,2,3,3,4,47,FALSE,Have,4.42,4.62,0,0.2
5,6,2,3,3,4,47,FALSE,you,4.62,4.72,0,0.1
5,6,2,3,3,4,47,FALSE,ever,4.76,5.05,0,0.29
5,6,2,3,3,4,47,FALSE,that,5.07,5.38,0,0.31
5,6,2,3,2,4,47,FALSE,of,5.38,5.5,0,0.12
5,6,2,3,2,4,41,FALSE,making,5.51,5.92,0,0.41
5,6,2,3,2,4,41,FALSE,your,5.92,6.16,0,0.24
5,6,2,3,2,4,41,FALSE,own,6.2,6.49,0,0.29
5,6,2,3,2,4,41,FALSE,ani mation,6.54,7.13,0,0.59
5,5,2,3,2,4,41,FALSE,show,7.13,7.46,0,0.33
5,5,2,3,2,4,41,FALSE,well,7.98,8.26,0,0.28
5,5,2,3,2,4,4,FALSE,I,8.32,8.63,0,0.31
5,5,2,3,2,4,4,FALSE,did,8.64,9.2,0,0.56
5,8,2,3,1,4,4,FALSE,but,9.46,9.87,0,0.41
5,8,2,3,1,4,22,FALSE,I,10.01,10.19,0,0.18
5,8,2,3,1,4,22,FALSE,don't,10.19,10.47,0,0.28
5,8,2,3,1,4,22,FALSE,know,10.48,10.74,0,0.26
5,8,2,3,3,4,22,FALSE,the,10.75,10.77,1.5,0.02
5,8,1,3,3,4,22,FALSE,first,10.78,11.04,1.5,0.26
5,8,1,3,3,4,22,FALSE,thing,11.05,11.26,1.5,0.21
5,8,1,3,3,4,22,FALSE,about,11.27,11.56,1.5,0.29
5,8,1,3,3,4,22,FALSE,ani mation,11.74,12.24,1.5,0.5
5,1,2,3,3,4,3,FALSE,So,12.75,13.27,0,0.52
5,1,2,3,2,4,3,FALSE,I,13.45,13.63,0,0.18
5,1,2,3,2,4,3,FALSE,start,13.63,14.02,0,0.39
5,1,2,3,2,4,3,FALSE,to,14.03,14.05,0,0.02
5,1,2,3,2,4,3,FALSE,learn,14.049999,14.299999,0,0.25
5,1,2,3,2,4,3,FALSE,how,14.46,14.69,0,0.23
5,1,2,3,2,4,3,FALSE,to,14.719999,14.859999,0,0.14
5,1,2,3,3,4,3,FALSE,draw,14.9,15.39,0,0.49
5,1,2,3,3,4,3,FALSE,and,15.46,15.71,0,0.25
5,1,2,3,1,4,3,FALSE,lurn,15.71,16,0,0.29
5,1,2,3,1,4,10,FALSE,about,16.02,16.35,0,0.33
5,1,2,3,1,4,10,FALSE,ani mation,16.549999,17.069999,0,0.52
5,4,2,3,2,4,10,FALSE,It,17.5,17.79,0,0.29
5,4,2,3,2,4,10,FALSE,was,17.789999,17.999999,1.5,0.21
5,4,2,3,2,4,10,FALSE,hard,18.01,18.38,1.5,0.37
5,4,2,3,2,4,10,FALSE,at,18.379999,18.539999,1.5,0.16
5,4,2,3,2,4,10,FALSE,first,18.65,18.97,1.5,0.32
5,1,2,3,2,4,16,FALSE,but,18.99,19.2,0,0.21
5,1,2,3,2,4,16,FALSE,I,19.2,19.43,0,0.23
5,1,2,3,2,4,16,FALSE,got,19.45,19.71,0,0.26
5,1,2,3,2,4,16,FALSE,the,19.72,19.85,0,0.13
5,1,2,3,3,4,16,FALSE,hang,19.85,20.16,0,0.31
5,1,2,3,3,4,16,FALSE,of,20.16,20.34,0,0.18
5,1,2,3,3,4,16,FALSE,it,20.34,20.52,0,0.18
5,1,2,3,3,4,16,FALSE,after,20.56,20.94,0,0.38
5,1,2,3,3,4,16,FALSE,a,20.94,21.01,0,0.07
5,1,2,3,3,4,16,FALSE,val,21.01,21.37,0,0.36
5,2,2,3,2,4,13,FALSE,but,21.8,22.29,0,0.49
5,2,2,3,2,4,13,FALSE,it,22.48,22.68,0,0.2
5,2,2,3,2,4,13,FALSE,took,22.74,22.98,0,0.24
5,2,2,3,2,4,13,FALSE,a,23.02,23.12,0,0.1
5,2,2,3,2,4,13,FALSE,lot,23.12,23.35,0,0.23
5,2,2,3,2,4,13,FALSE,of,23.35,23.51,0,0.16
5,2,2,3,2,4,13,FALSE,time,23.54,23.92,0,0.38
5,2,2,3,2,4,13,FALSE,cre tin,23.97,24.43,0,0.46
5,2,2,3,2,4,13,FALSE,one,24.43,24.68,0,0.25
5,2,2,3,2,4,13,FALSE,mi nut,24.68,24.99,0,0.31
5,2,2,3,2,4,13,FALSE,of,25.02,25.3,0,0.28
5,2,1,3,3,4,13,FALSE,mouth,25.36,25.78,0,0.42
5,2,1,3,3,4,13,FALSE,movement,25.85,26.43,0,0.58
5,2,1,3,3,4,3,FALSE,takes,26.44,26.76,1.5,0.32
5,2,1,3,3,4,3,FALSE,me,26.809999,27.009999,1.5,0.2
5,2,1,3,3,4,3,FALSE,a round,27.02,27.38,1.5,0.36
5,2,1,3,3,4,3,FALSE,one,27.389999,27.649999,1.5,0.26
5,2,1,3,3,4,3,FALSE,hour,27.65,27.72,1.5,0.07
5,2,1,3,2,4,3,FALSE,work,27.719999,27.749999,1.5,0.03
5,8,2,3,2,4,2,FALSE,it,27.75,27.77,0,0.02
5,8,2,3,2,4,2,FALSE,was,28.91,29.17,0,0.26
5,8,2,3,2,4,2,FALSE,fun,29.18,29.58,0,0.4
5,8,2,3,2,4,2,FALSE,at,29.58,29.58,0,0
5,8,2,3,2,4,2,FALSE,the,29.8,29.9,0,0.1
5,8,2,3,2,4,2,FALSE,beg ning,29.9,30.57,0,0.67
5,4,2,3,2,4,2,FALSE,but,30.65,30.86,0,0.21
5,4,2,3,2,4,2,FALSE,I,30.88,31.12,0,0.24
5,4,2,3,2,4,2,FALSE,got,31.13,31.31,0,0.18
5,4,2,3,3,4,2,FALSE,bored,31.349999,31.759999,0,0.41
5,4,2,3,3,4,28,FALSE,doing,31.78,32.1,0,0.32
5,4,2,3,3,4,28,FALSE,it,32.11,32.3,0,0.19
5,4,1,3,3,4,28,FALSE,b cas,32.77,33.1,0,0.33
5,4,1,3,3,4,28,FALSE,it,33.12,33.37,0,0.25
5,4,1,3,2,4,28,FALSE,was,33.37,33.53,0,0.16
5,4,1,3,2,4,28,FALSE,a,33.53,33.54,0,0.01
5,4,1,3,2,4,28,FALSE,re peet,33.67,34.17,0,0.5
5,4,2,3,2,4,28,FALSE,pro ces,34.17,34.72,0,0.55
5,4,2,3,2,4,28,FALSE,and,34.74,34.99,0,0.25
5,4,2,3,2,4,16,FALSE,I,35,35.29,0,0.29
5,4,2,3,2,4,16,FALSE,hate,35.299999,35.629999,1.5,0.33
5,4,2,3,2,4,16,FALSE,re petin,35.690001,36.090001,1.5,0.4
5,4,2,3,2,4,16,FALSE,pro ces,36.090001,36.790001,1.5,0.7
5,6,2,3,2,4,16,FALSE,so,37.24,37.7,0,0.46
5,6,2,3,2,4,16,FALSE,I,38,38.17,0,0.17
5,6,2,3,2,4,16,FALSE,started,38.17,38.53,0,0.36
5,6,2,3,2,4,19,FALSE,looking,38.53,38.83,0,0.3
5,6,2,3,2,4,19,FALSE,for,38.83,39.06,0,0.23
5,6,2,3,2,4,19,FALSE,a,39.09,39.2,0,0.11
5,6,2,3,2,4,19,FALSE,way,39.2,39.45,0,0.25
5,6,2,3,2,4,19,FALSE,to,39.45,39.61,0,0.16
5,6,2,3,2,4,19,FALSE,a to ma tion,39.64,40.13,0,0.49
5,6,2,3,2,4,19,FALSE,the,40.17,40.26,0,0.09
5,6,2,3,2,4,19,FALSE,process,40.26,40.86,0,0.6
5,1,2,3,2,4,34,FALSE,so,41.6,41.98,0,0.38
5,1,2,3,3,4,34,FALSE,I,42.01,42.24,0,0.23
5,1,2,3,3,4,34,FALSE,start,42.25,42.64,0,0.39
5,1,2,3,3,4,34,FALSE,watching,42.67,43.14,0,0.47
5,7,1,3,3,4,34,FALSE,other,43.18,43.43,0,0.25
5,7,1,3,3,4,34,FALSE,not,43.43,43.7,0,0.27
5,7,1,3,3,4,34,FALSE,so,43.7,43.88,0,0.18
5,7,1,3,3,4,34,FALSE,cool,43.88,44.2,0,0.32
5,7,1,3,3,4,34,FALSE,a to ma tion,44.24,45.07,0,0.83
5,7,2,3,1,4,34,FALSE,videos,45.08,45.48,0,0.4
5,7,2,3,1,4,40,FALSE,on,45.52,45.72,0,0.2
5,7,2,3,1,4,40,FALSE,a,45.719999,45.779999,0,0.06
5,7,2,3,1,4,40,FALSE,different,45.78,46.21,0,0.43
5,7,2,3,1,4,40,FALSE,channel,46.21,46.45,0,0.24
5,1,2,3,2,4,40,FALSE,I,47.08,47.19,1.5,0.11
5,1,2,3,2,4,19,FALSE,re liz,47.19,47.7,1.5,0.51
5,1,2,3,2,4,19,FALSE,some,47.719999,47.939999,1.5,0.22
5,1,2,3,2,4,19,FALSE,of,47.94,48.06,1.5,0.12
5,1,2,3,2,4,19,FALSE,the,48.07,48.18,1.5,0.11
5,1,2,3,2,4,19,FALSE,pro ces,48.179999,48.969999,0,0.79
5,1,2,3,2,4,19,FALSE,are,49.009999,49.299999,0,0.29
5,1,2,3,2,4,19,FALSE,re peat ,49.299999,49.919999,0,0.62
5,6,2,3,2,4,19,FALSE,for,50.07,50.27,0,0.2
5,6,2,3,2,4,19,FALSE,exam pal,50.27,50.95,0,0.68
5,6,2,3,1,4,3,FALSE,mouth,50.96,51.27,2,0.31
5,6,2,3,1,4,3,FALSE,mo ment,51.309999,51.819999,2,0.51
5,6,2,3,3,4,3,FALSE,eyes,51.849999,52.339999,2,0.49
5,1,2,3,3,4,3,FALSE,and,52.369999,52.569999,2,0.2
5,1,2,3,2,4,3,FALSE,emotion,52.59,53.23,2,0.64
5,1,2,3,2,4,3,FALSE,I,54,54.11,2,0.11
5,1,2,3,2,4,3,FALSE,thought,54.109999,54.339999,0,0.23
5,1,2,3,2,4,19,FALSE,I,54.34,54.43,0,0.09
5,1,2,3,2,4,19,FALSE,can,54.43,54.67,0,0.24
5,1,2,3,2,4,19,FALSE,a to ma tion,54.71,55.11,0,0.4
5,1,2,3,2,4,19,FALSE,this,55.16,55.34,0,0.18
5,1,2,3,2,4,19,FALSE,process,55.34,55.79,0,0.45
5,1,2,3,3,4,19,FALSE,with,56.38,56.5,0,0.12
5,1,2,3,3,4,19,FALSE,the,56.51,56.63,0,0.12
5,1,2,3,3,4,19,FALSE,help,56.63,56.88,0,0.25
5,1,2,3,3,4,19,FALSE,of,56.88,57.07,0,0.19
5,1,2,3,3,4,19,FALSE,cary  k h,57.08,57.75,0,0.67
5,1,2,3,3,4,9,FALSE,ideas,57.79,58.31,0,0.52
5,1,2,3,3,4,9,FALSE,and,58.31,58.51,0,0.2
5,1,2,3,3,4,9,FALSE,its,58.51,58.75,0,0.24
5,1,2,3,3,4,9,FALSE,channel,58.75,59.21,1.5,0.46
5,1,2,3,2,4,9,FALSE,the,60.02,60.31,1.5,0.29
5,1,2,3,2,4,9,FALSE,dream,60.32,60.55,1.5,0.23
5,1,2,3,2,4,9,FALSE,become,60.55,60.85,1.5,0.3
5,1,2,3,2,4,9,FALSE,reality,60.85,61.45,1.5,0.6
5,1,1,3,2,4,42,FALSE,I,61.98,62.23,0,0.25
5,1,1,3,2,4,42,FALSE,made,62.27,62.55,0,0.28
5,1,1,3,3,4,42,FALSE,this,62.55,62.71,0,0.16
5,1,1,3,3,4,42,FALSE,software,62.71,63.26,0,0.55
5,6,2,3,3,4,42,FALSE,in,64.08,64.27,0,0.19
5,6,2,3,3,4,42,FALSE,it,64.27,64.39,0,0.12
5,6,2,3,3,4,47,FALSE,you,64.429999,64.569999,0,0.14
5,6,2,3,3,4,47,FALSE,don't,64.57,64.83,0,0.26
5,6,2,3,2,4,47,FALSE,have,64.83,65.04,0,0.21
5,6,2,3,2,4,47,FALSE,to,65.04,65.16,1.5,0.12
5,6,2,3,2,4,47,FALSE,worry,65.17,65.48,1.5,0.31
5,6,2,3,2,4,47,FALSE,about,65.48,65.86,1.5,0.38
5,6,2,3,2,4,47,FALSE,any,65.94,66.3,1.5,0.36
5,6,2,3,2,4,47,FALSE,animation,66.32,66.98,1.5,0.66
5,1,2,3,2,4,47,FALSE,drawing,66.99,67.65,1.5,0.66
5,1,2,3,2,4,46,FALSE,all,67.78,68.02,0,0.24
5,1,2,3,2,4,46,FALSE,you,68.02,68.18,0,0.16
5,1,2,3,2,4,46,FALSE,have,68.179999,68.339999,0,0.16
5,1,2,3,2,4,46,FALSE,to,68.34,68.47,0,0.13

"""
out_csv= f"""character,emotion,intensity,head_direction,eyes_direction,screen_mode,body_action,reaction_bool,word,init,final,room
,,,,,,,,your,0.39,0.51,0
,,,,,,,,password,0.52,0.9,0
,,,,,,,,to,0.99,1.11,0
,,,,,,,,something,1.12,1.49,0
,,,,,,,,new,1.5,1.68,0
,,,,,,,,ok,1.87,2.16,1.5
,,,,,,,,cool,2.27,2.51,1.5
,,,,,,,,what,2.76,2.89,0
,,,,,,,,do,2.9,2.92,0
,,,,,,,,you,2.93,2.99,0
,,,,,,,,want,3,3.15,0
,,,,,,,,it,3.16,3.3,0
,,,,,,,,be,3.31,3.53,0
,,,,,,,,amm,3.82,4.31,0
,,,,,,,,Tequila,5.19,5.58,0
,,,,,,,,you,5.8,5.92,0
,,,,,,,,cant,5.93,6.12,0
,,,,,,,,make,6.13,6.25,0
,,,,,,,,it,6.26,6.33,0
,,,,,,,,so,6.34,6.49,0
,,,,,,,,obvious,6.5,6.87,0
,,,,,,,,man,6.88,7.11,0
,,,,,,,,its,7.26,7.35,0
,,,,,,,,got,7.36,7.47,0
,,,,,,,,be,7.5,7.61,0
,,,,,,,,something,7.62,7.82,0
,,,,,,,,i,7.83,7.89,0
,,,,,,,,can,7.9,8.01,0
,,,,,,,,remember,8.02,8.38,0
,,,,,,,,though,8.39,8.61,0
,,,,,,,,you,8.69,8.78,0
,,,,,,,,know,8.79,8.99,0
,,,,,,,,and,9.34,9.46,0
,,,,,,,,i,9.47,9.48,0
,,,,,,,,never,9.49,9.71,0
,,,,,,,,forget,9.72,9.98,0
,,,,,,,,Tequila,9.99,10.4,1.5
,,,,,,,,unless,11.46,11.75,1.5
,,,,,,,,i,11.76,11.81,1.5
,,,,,,,,drink,11.82,12.01,1.5
,,,,,,,,too,12.02,12.06,1.5
,,,,,,,,much,12.09,12.29,1.5
,,,,,,,,Tequila,12.3,12.64,0
,,,,,,,,than,12.83,13.05,0
,,,,,,,,i,13.6,13.66,0
,,,,,,,,forget,13.67,13.93,0
,,,,,,,,everything,13.94,14.27,0
,,,,,,,,whats,14.32,14.49,0
,,,,,,,,your,14.5,14.59,0
,,,,,,,,wife's,14.6,14.89,0
,,,,,,,,name,14.9,15.11,0
,,,,,,,,wowowowo,15.19,16.13,1.5
,,,,,,,,relax,16.19,16.63,1.5
,,,,,,,,why,16.68,16.77,0
,,,,,,,,are,16.78,16.78,0
,,,,,,,,we,16.79,16.89,0
,,,,,,,,bringing,16.9,17.11,0
,,,,,,,,her,17.12,17.21,0
,,,,,,,,into,17.22,17.36,0
,,,,,,,,this,17.37,17.55,0
,,,,,,,,its,17.56,17.61,0
,,,,,,,,got,17.62,17.77,0
,,,,,,,,to,17.78,17.83,0
,,,,,,,,be,17.84,17.93,0
,,,,,,,,something,17.94,18.21,0
,,,,,,,,other,18.24,18.45,0
,,,,,,,,than,18.46,18.59,0
,,,,,,,,Tequila,18.63,19.08,0
,,,,,,,,whats,19.27,19.46,1.5
,,,,,,,,your,19.47,19.57,1.5
,,,,,,,,favorite,19.58,19.76,1.5
,,,,,,,,word,19.77,20.07,1.5
,,,,,,,,amm,20.11,20.73,0
,,,,,,,,Tequila,21.19,21.62,0

"""
assets_data = str({
        "character": {
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "10": "10",
        },
        "emotion": {
            "1": "happy",
            "2": "sad",
            "3": "angry",
            "4": "bore",
            "5": "content",
            "6": "glare",
            "7": "sarcasm",
            "8": "worried",
            "9": "crazy",
            "10": "evil_laugh",
            "11": "lust",
            "12": "shock",
            "13": "silly",
            "14": "spoked",
        },
        "intensity": {"1": True, "2": False},
        "head_direction": {"1": "L", "2": "M", "3": "R"},
        "eyes_direction": {"1": "L", "2": "M", "3": "R"},
        "screen_mode": {
            "1": "office",
            "2": "explaination",
            "3": "white",
            "4": "plain",
            "5": "green",
        },
        "body_action": {
            "1": "achieve",
            "2": "answer",
            "3": "explain",
            "4": "me",
            "5": "not_me",
            "6": "question",
            "7": "technical",
            "8": "why",
            "9": "achieve",
            "10": "answer",
            "11": "chilling",
            "12": "come",
            "13": "confuse",
            "14": "crazy",
            "15": "dancing",
            "16": "explain",
            "17": "feeling_down",
            "18": "hi",
            "19": "i",
            "20": "idea",
            "21": "idk",
            "22": "joy",
            "23": "jumping",
            "24": "kung_fu",
            "25": "love",
            "27": "meditation",
            "28": "model",
            "30": "paper",
            "31": "praying",
            "32": "question",
            "33": "running",
            "34": "search",
            "35": "shy",
            "36": "singing",
            "37": "sneaky",
            "38": "standing",
            "39": "technical",
            "40": "that",
            "41": "thinking",
            "42": "this",
            "43": "what",
            "44": "why",
            "45": "winner",
            "46": "yeah",
            "47": "you",
        },
        "reaction": {
            "1": "happy",
            "2": "sad",
            "3": "angry",
            "4": "bore",
            "5": "content",
            "6": "glare",
            "7": "scard",
            "8": "worried",
        },
})
prompt = f"""

Your task involves filling out the remaining values in the out-csv CSV file based on your judgment. It's crucial to ensure that the values you add are within the bounds of the assets_data JSON.
The assets_data JSON, which I will provide, contains all the assets that can be utilized in the out-csv CSV file.
I will also share an example_data CSV file to help you understand the desired format of the final CSV. Your goal is to create a CSV file that matches this example. Remember, the values you're adding pertain to the animation character's reactions to each word specified in the word field.
Here's an illustrative example of how the filled out-csv might appear for a new row with some missing data:

character,emotion,intensity,head_direction,eyes_direction,screen_mode,body_action,reaction_bool,word,init,final,room 7,3,1,3,2,3,?,FALSE,excited,1.0,2.3,0.5


In this example:

- **Character**: A match was found in `assets_data` (character: {{'7': '7'}}...), so "7" is copied. All of them are different characters.
- **Emotion**: A match was found in `assets_data` (emotion: {{'3': 'angry'}}...), so "3" is copied based on your judgment of what emotion of eyes should be added for the given word.
- **Intensity**: A match was found in `assets_data` (intensity: {{'1': True}}), so "1" is copied based on intensity strong emotion or normal.
- **Head_direction**: There was no match or value outside the range (1-3) in `assets_data`, so based on the word where the head_direction should move, we copy from 1 to 3 ({{"1": "L", "2": "M", "3": "R"}} L=left, M=mid, R=Right).
- **Eyes_direction**: A match was found in `assets_data` (eyes_direction: {{'2': 'M'}}), so based on the word where the eyes_direction should move, we copy from 1 to 3 ({{"1": "L", "2": "M", "3": "R"}} L=left, M=mid, R=Right).
- **Screen_mode**: You must select from "screen_mode": {{
            "1": "office",
            "2": "explanation",
            "3": "white",
            "4": "plain",
            "5": "green",
        }}
from 1 to 5 based on your judgment regarding what background should be added.
- **Body_action**: You must select a body type from ("body_action": {{'1': 'achieve'}},,,) based on your judgment regarding what body movement should be added.
- **Reaction_bool**: A match was found in `assets_data` (reaction: {{'1': 'happy'}}), so "FALSE" is copied (assuming this is a boolean field based on the example data).
- **Word, init, final, room**: These values cannot be filled in as they will be provided.

The following is the list of data.

assets_data: ```{assets_data!r}```
example_data: ```{example_data!r}```
out-csv: ```{out_csv!r}```
"""


print(prompt)
with open("myfile.txt", "w") as file1:
    # Writing data to a file
      file1.write(prompt)

response = get_completion(prompt, temperature=0)
print(response.content)
with open("output.txt", "w") as output:
      output.write(response.content)

