import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) # 속도 조절

    engine.say(text)
    engine.runAndWait()

speak("안녕하세요.챗GPT로 만드는 파이썬입니다.")
    