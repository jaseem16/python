import requests

city = input("Enter city: ")
api = f"https://wttr.in/{city}?format=3"

print(requests.get(api).text)
