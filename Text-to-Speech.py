from gtts import gTTS

text = input("Enter text: ")
audio = gTTS(text)
audio.save("voice.mp3")
print("Audio saved!")
