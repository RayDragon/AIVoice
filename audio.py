import speech_recognition as sr
from gtts import gTTS as gts
import os
import pygame

r = sr.Recognizer()
m = sr.Microphone()
pygame.init()
pygame.mixer.init()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to ", r.energy_threshold)
    while True:
        print("Ready to record....:")
        with m as source: audio = r.listen(source)
        print("Let me recognise it :) ")
        try:
            value = r.recognize_sphinx(audio)
            tts = gts(text='you said,' + value, lang='en')
            filename = 'temp.mp3'
            tts.save(filename)

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            print(value)
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            os.remove(filename)  # remove temperory file
            if value == 'exit' or value == 'Exit':
                break

        except sr.UnknownValueError:
            print("Didn't catch that")
        except sr.RequestError as e:
            print("Internet Required {0}".format(e))

except KeyboardInterrupt:
    pass