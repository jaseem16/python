
while True:
    user = input("You: ")

    if "hello" in user.lower():
        print("Bot: Hello!")
    elif "bye" in user.lower():
        print("Bot: Bye!")
        break
    else:
        print("Bot: I don't understand.")
