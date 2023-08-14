from gtts import gTTS
from playsound import playsound

# 오류 발생한 경우 아래와 같이 모듈 재설치
# 지정한 명령 매개 변수를 드라이버가 인식할 수 없습니다. 
# pip install playsound==1.2.2

#1. 텍스트 입력
text = input("텍스트를 입력하세요: ")

#2. 한국어 음성 출력 설정
tts = gTTS(text, lang="ko")

#3. 음성을 mp3 파일로 저장
tts.save('mp3/output.mp3')

#4. mp3 재생
playsound('mp3/output.mp3')