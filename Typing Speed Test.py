import time

text = "Python is a powerful programming language."
print(text)

start = time.time()
user = input("Start typing: ")
end = time.time()

words = len(user.split())
wpm = words / ((end - start) / 60)
print("Your WPM:", round(wpm))
