import pyfiglet
from colorama import Fore, init

init(autoreset=True)

user_text = input("Masukkan teks yang ingin ditampilkan: ")
banner = pyfiglet.figlet_format(user_text, font="slant")
print(Fore.MAGENTA + banner)

