import os
import random

def text_to_speech(text):
    try:
        command = f'powershell -command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{text}\')"'
        os.system(command)
    except Exception as e:
        print(f"An error occurred: {e}")

def greet_user():
    greetings = [
        "Welcome to the Python Text-to-Speech !",
        "Hello there! ",
        "Greetings, human! Let's have some fun with words!",
    ]
    print(random.choice(greetings))

def main():
    greet_user()

    while True:
        Speak = input("Enter the text you want to speak (type 'stop' to exit): ")

        if Speak.lower() == 'stop':
            print("\nGoodbye! It was great having fun with you.")
            break
        elif Speak.lower() == "fact":
            tell_fact()
        else:
            text_to_speech(Speak)

def tell_fact():
    facts = [
        "Polar bears are nearly undetectable by infrared cameras because they are so well-insulated." or
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896; it lasted just 38 minutes."or
        "The unicorn is Scotland's national animal.",
    ]
    fact = random.choice(facts)
    print(f"Here's a fact for you: {facts}")
    text_to_speech(fact)

if __name__ == '__main__':
    main()
