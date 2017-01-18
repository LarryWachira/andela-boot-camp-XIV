import requests

response = requests.get("http://api.open-notify.org/arson.json")
info = response.json

if response.status_code == 200:
    print("Want to play 'Guess how many people are in space'?\nType Y or N:")
    answer = input('> ')

    if answer == 'Y' or answer == 'y':
        print("Well, what are you waiting for? Guess how many humans are in space right now:\n> ")
        answer = input()

        if answer == info["number"]:
            print("Of course. Google, right? \n\n:( ")
        else:
            print("Wrong! There are {} people in space right now.").format(info["number"])
            print("\n That'll be one billion dollars. I'll take cash.")

    elif answer == 'N' or answer == 'n':
        print("You must be a lot of fun at parties. \n\n:(")

    else: print("Seriously?")

else: print("Server Unavailable")