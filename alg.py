import requests
import colorama
import os
from colorama import *

#Banner

def banner():
    os.system('cls')
    print(f'''{Fore.YELLOW}
                ▄▄                            ▄▄        ▄▄                         
      ██      ▀███                            ██   ██  ███                         
     ▄██▄       ██                                 ██   ██                         
    ▄█▀██▄      ██  ▄█▀█████ ▄██▀██▄▀███▄███▀███ ██████ ███████▄ ▀████████▄█████▄  
   ▄█  ▀██      ██ ▄██  ██  ██▀   ▀██ ██▀ ▀▀  ██   ██   ██    ██   ██    ██    ██  
   ████████     ██ ▀█████▀  ██     ██ ██      ██   ██   ██    ██   ██    ██    ██  
  █▀      ██    ██ ██       ██▄   ▄██ ██      ██   ██   ██    ██   ██    ██    ██  
▄███▄   ▄████▄▄████▄███████  ▀█████▀▄████▄  ▄████▄ ▀███████  ████▄████  ████  ████▄
                   █▀     ██                                                       
                   ██████▀                                                         
                                                            
                                         
    ''')
    github()

# List selection/registrated names and unreged

def github():
    list = str(input("List (list.txt): "))
    with open(list, 'r') as h:
        usernames = [ line.strip() for line in h.read().split('\n') if line ]
        for name in usernames:
            r = requests.get(f"https://github.com/" + name)
            if f"{name} doesn't have any public repositories yet." in r.text or 'Popular repositories' in r.text or 'Repositories' in r.text:
                print(f'{Fore.RED}[✗]{Fore.WHITE} {name} is taken')
                with open('checked.txt', 'a') as h:
                    h.write(name + ' is taken' +'\n')
            elif r.status_code == 404:
                print(f'{Fore.GREEN}[✓]{Fore.WHITE} {name} is not taken')
                with open('checked.txt', 'a') as h:
                    h.write(name + 'is not taken' + '\n')
            elif 'rate' or 'Rate' in r.text:
                print(f'{Fore.YELLOW}[!]{Fore.WHITE} Rate Limited')
                with open('checked.txt', 'a') as h:
                  h.write(name + ' was rate limted' + '\n')
            else: 
                print(f'{Fore.RED}[✗]{Fore.WHITE} {name} is taken')
            
        
banner()
