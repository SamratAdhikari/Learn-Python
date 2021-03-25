# News Reader


import requests
import json
a = 0
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    print("News for today....\n")
    speak("News for today")
    url = "https://nepalcorona.info/api/v1/data/nepal"
    news = requests.get(url).text
    #print(news)
    news_dict = json.loads(news)

    # print(news_dict)
    for i in news_dict:
        # print(f"{i} : {news_dict[i]}")
        print(f"{i} : {news_dict[i]}")
        speak(f"{i} : {news_dict[i]}")
        a += 1
        if a == 9:
            break
    print("Thats all for now.. Thank you...")
    speak("Thats all for now.. Thank you...")



input("This program is exiting... Press Enter")