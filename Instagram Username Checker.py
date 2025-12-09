import requests

username = input("Enter username: ")
url = f"https://www.instagram.com/{username}/"

r = requests.get(url)

if r.status_code == 200:
    print("Username exists!")
else:
    print("Username not found.")
