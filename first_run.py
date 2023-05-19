import os 
from colorama import Fore

print(Fore.GREEN + 'Installing Dependencies...')

os.system("pip install -r requirements.txt")
os.system('cls')
print(Fore.YELLOW + 'Launching Terminals...Please Login With Three Different Accounts')
os.system('start cmd /k python c1.py')
os.system('start cmd /k python c2.py')
os.system('start cmd /k python c3.py')