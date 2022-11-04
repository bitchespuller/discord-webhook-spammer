import requests
from colorama import *
import time
discord_webhook_url = ""

print(f""" {Fore.RED}

     ____  __  ______  _   _______  __    _       ____________       _____ ____  ___    __  _____  _____________ 
   / __ \/ / / / __ \/ | / /  _/ |/ /   | |     / / ____/ __ )     / ___// __ \/   |  /  |/  /  |/  / ____/ __ /
  / /_/ / /_/ / / / /  |/ // / |   /    | | /| / / __/ / __  |_____\__ \/ /_/ / /| | / /|_/ / /|_/ / __/ / /_/ /
 / ____/ __  / /_/ / /|  // / /   |     | |/ |/ / /___/ /_/ /_____/__/ / ____/ ___ |/ /  / / /  / / /___/ _, _/ 
/_/   /_/ /_/\____/_/ |_/___//_/|_|     |__/|__/_____/_____/     /____/_/   /_/  |_/_/  /_/_/  /_/_____/_/ |_|                                                                                                                       

""")




Message = {
  "content": input("Message -> ")
}

print("Starting!")
time.sleep(2)
def spam():
    while(True):
        print(f'{Fore.LIGHTGREEN_EX}[+] Sent!')
        requests.post(discord_webhook_url, data=Message)
spam()
