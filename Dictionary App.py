import requests

word = input("Enter word: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

res = requests.get(url).json()
print(res[0]["meanings"][0]["definitions"][0]["definition"])
