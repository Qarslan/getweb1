import pyfiglet
from colorama import Fore, init

# Inisialisasi Colorama
init(autoreset=True)

# Membuat banner dengan pyfiglet
banner = pyfiglet.figlet_format("WELCOME", font="slant")

# Menampilkan banner dengan warna
print(Fore.CYAN + banner)
print(Fore.GREEN + "Selamat datang di program kami!")
