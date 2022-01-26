'''
from gtts import gTTS
import playsound
tts = gTTS(text='ยินดีต้อนรับค่ะ',lang='th')
tts.save('welcome.mp3')
playsound.playsound('welcome.mp3')

import pyttsx3
engine = pyttsx3.init()
engine.say("lap thana chai")
engine.runAndWait()
'''
from gtts import gTTS
import playsound
tts = gTTS(text='Hello',lang='en')
tts.save('hello.mp3')
playsound.playsound('hello.mp3',True)
