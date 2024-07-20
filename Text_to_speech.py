from gtts import gTTS
import os

language = "en-us"
text = (" Hello there this is a mp3 by python")
speech = gTTS(text=text, lang=language, slow=False, tld="com.au")
speech.save("texttospeech.mp3")
os.system("start texttospeech.mp3")
