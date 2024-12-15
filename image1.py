import requests
from PIL import Image
from io import BytesIO
from colorama import Fore, Style, init

# Inisialisasi Colorama
init(autoreset=True)

# Karakter ASCII diurutkan dari gelap ke terang
ASCII_CHARS = "@%#*+=-:. "

# Peta warna berdasarkan kecerahan
COLOR_MAP = [
    Fore.RED,          # Gelap sekali
    Fore.YELLOW,       # Gelap
    Fore.GREEN,        # Sedang
    Fore.CYAN,         # Terang
    Fore.BLUE,         # Terang sekali
    Fore.WHITE         # Putih
]

# Fungsi untuk mengunduh gambar dari URL
def download_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.exceptions.RequestException as e:
        print(f"Error: Tidak dapat mengunduh gambar. {e}")
        return None

# Fungsi untuk mengubah piksel menjadi karakter ASCII dengan warna
def pixel_to_colored_ascii(pixel, range_width):
    ascii_char = ASCII_CHARS[pixel // range_width]
    color = COLOR_MAP[min(pixel // (256 // len(COLOR_MAP)), len(COLOR_MAP) - 1)]
    return f"{color}{ascii_char}"

# Fungsi utama untuk menghasilkan ASCII-art berwarna
def generate_colored_ascii_art(image, new_width=100):
    try:
        # Ubah ukuran gambar sesuai lebar baru
        width, height = image.size
        aspect_ratio = height / width
        new_height = int(new_width * aspect_ratio * 0.55)  # Adjust ratio
        image = image.resize((new_width, new_height))

        # Konversi gambar ke skala abu-abu
        grayscale_img = image.convert("L")

        # Mengubah setiap piksel menjadi karakter ASCII dengan warna
        pixels = grayscale_img.getdata()
        range_width = 256 // len(ASCII_CHARS)  # Hitung rentang kecerahan per karakter
        ascii_str = "".join([pixel_to_colored_ascii(pixel, range_width) for pixel in pixels])

        # Membagi string ASCII menjadi baris
        ascii_lines = [ascii_str[index: index + new_width] for index in range(0, len(ascii_str), new_width)]
        return "\n".join(ascii_lines)
    except Exception as e:
        print(f"Error: Tidak dapat memproses gambar. {e}")
        return None

# Main Program
if __name__ == "__main__":
    # Meminta input URL dari pengguna
    image_url = input("Masukkan URL gambar: ")

    # Mengunduh gambar dari URL
    image = download_image(image_url)

    if image:
        # Menghasilkan ASCII-art berwarna
        ascii_art = generate_colored_ascii_art(image, new_width=80)

        if ascii_art:
            print("\n=== ASCII Art Berwarna ===\n")
            print(ascii_art)
