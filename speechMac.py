#import pyaudio
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
"""import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("demo.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("You said " + r.recognize(audio))         # recognize speech using Google Speech Recognition
except KeyError:                                    # the API key didn't work
    print("Invalid API key or quota maxed out")
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")"""
"""from pygsr import Pygsr
speech = Pygsr()
speech.record(3) # duration in seconds (3)
phrase, complete_response = speech.speech_to_text('es_ES') # select the language
print phrase"""