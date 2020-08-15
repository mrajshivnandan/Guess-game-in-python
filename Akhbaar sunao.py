# Akhbaar Padhke Sunao
from win32com.client import Dispatch
import requests
import json
def speak(str):
    speak= Dispatch('SAPI.SpVoice')
    speak.Speak(str)
# 74bee1588dc24458a311140342832ccc
di1 = {1: 'business', 2: 'entertainment', 3: 'general', 4: 'health', 5: 'science', 6: 'sports', 7: 'technology'}

if __name__=='__main__':
    k= input('Enter Your API Key (If you dont have API Key then go to http://newsapi.org\n')
    print("Select Topic:")
    for key, value in di1.items():
        print("Press", key, "for", value, "\n", end="")
    t = int(input())

    speak(f"News of today for {di1[t]}")
    url= f"http://newsapi.org/v2/top-headlines?country=in&category={di1[t]}&apiKey={k}"
    news= requests.get(url).text
    news_= json.loads(news)
    arti= news_['articles']
    n = 1
    for article in arti:

        print(f'---------------News number {n} --------------')
        print(article['title'])
        speak(article['title'])
        print(article["description"])
        speak(article["description"])
        print('For more details visit ', article['url'])
        speak("Moving on to the next news..")
        n= n+1
