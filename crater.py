from colorama import *
from art import *
import requests
import os

from requests import status_codes


banner = """
       _..._                                                           
    .-'_..._''.                                                        
  .' .'      '.\                                __.....__              
 / .'                                       .-''         '.            
. '             .-,.--.               .|   /     .-''"'-.  `. .-,.--.  
| |             |  .-. |    __      .' |_ /     /________\   \|  .-. | 
| |             | |  | | .:--.'.  .'     ||                  || |  | | 
. '             | |  | |/ |   \ |'--.  .-'\    .-------------'| |  | | 
 \ '.          .| |  '- `" __ | |   |  |   \    '-.____...---.| |  '-  
  '. `._____.-'/| |      .'.''| |   |  |    `.             .' | |      
    `-.______ / | |     / /   | |_  |  '.'    `''-...... -'   | |      
             `  |_|     \ \._,\ '/  |   /                     |_|      
                         `--'  `"   `'-'                              """
def menu():
    os.system("cls && title Crater")
    print(Fore.LIGHTBLUE_EX + banner + Fore.RESET)

    try:
        url = input("\nUrl "+ Fore.LIGHTRED_EX + "> "+ Fore.RED)
        r = requests.get(url)
        print(r)
        if status_codes == "200":
            print(+Fore.RESET+ Fore.RED + "Site down" + Fore.RESET)
            input("")
        
        else:
            print(+Fore.RESET+ Fore.GREEN + "Site en ligne" + Fore.RESET)
            input("")
    except:
        pass
        input("Press enter for close")

menu()
