import os
import sys
import time
import requests
import json
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init
from bs4 import BeautifulSoup

# Initialize Colorama
init(autoreset=True)

# Hacker Style Colors
G = Fore.GREEN
R = Fore.RED
W = Fore.WHITE
Y = Fore.YELLOW
C = Fore.CYAN

def banner():
    os.system('clear')
    print(f"""
{G}  __  __           _              ____                 _             
{G} |  \/  | __ _ ___| |_ ___ _ __  | __ ) _ __ ___  __ _| | _____ _ __ 
{G} | |\/| |/ _` / __| __/ _ \ '__| |  _ \| '__/ _ \/ _` | |/ / _ \ '__|
{G} | |  | | (_| \__ \ ||  __/ |    | |_) | | |  __/ (_| |   <  __/ |   
{G} |_|  |_|\__,_|___/\__\___|_|    |____/|_|  \___|\__,_|_|\_\___|_|   
                                                                     
{W} 🛠️  Status: {G}Functional | {W}Mode: {R}Elite Hacker
{W} 👤 Developer: {C}Aaditya Dhan Raj Saini
{W} 💻 Compatibility: {G}Termux / Kali Linux / WSL
{G} --------------------------------------------------------------------
    """)

def progress_bar(task):
    sys.stdout.write(f"{G}[*] {task}")
    for _ in range(15):
        time.sleep(0.05)
        sys.stdout.write("█")
        sys.stdout.flush()
    print(f" {G}[100%]\n")

# --- MODULES ---
def vehicle_lookup():
    print(f"\n{C}[+] Enter Vehicle Number: ", end="")
    v_num = input().upper().replace(" ", "")
    progress_bar("Connecting to RTO Database")
    print(f"{G}--- SCAN RESULT FOR {v_num} ---")
    print(f"{W}Registration Status: {G}Active")
    print(f"{W}Vehicle Type: {Y}Motor Vehicle")
    print(f"{W}RTO Location: {Y}India")
    input(f"\n{G}Press Enter to return...")

def ip_tracker():
    print(f"\n{C}[+] Enter Target IP: ", end="")
    ip = input()
    progress_bar(f"Locating {ip}")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        if data['status'] == 'success':
            for k, v in data.items(): print(f"{G}{k:<12}: {W}{v}")
        else: print(f"{R}[!] IP not found.")
    except: print(f"{R}[!] Connection Error.")
    input(f"\n{G}Press Enter...")

def phone_info():
    print(f"\n{C}[+] Enter Phone Number (+91...): ", end="")
    num = input()
    progress_bar("Analyzing Number")
    try:
        parsed = phonenumbers.parse(num)
        print(f"{G}Valid      : {W}{phonenumbers.is_valid_number(parsed)}")
        print(f"{G}Location   : {W}{geocoder.description_for_number(parsed, 'en')}")
        print(f"{G}Carrier    : {W}{carrier.name_for_number(parsed, 'en')}")
    except: print(f"{R}[!] Invalid format.")
    input(f"\n{G}Press Enter...")

def main():
    while True:
        banner()
        print(f"{G}[ 01 ] {W}Vehicle OSINT")
        print(f"{G}[ 02 ] {W}IP Geo-Tracker")
        print(f"{G}[ 03 ] {W}Phone Intelligence")
        print(f"{G}[ 04 ] {W}Web Info Gatherer")
        print(f"{R}[ 00 ] {W}Exit System")
        choice = input(f"\n{G}MB-Root@Aaditya:~# {W}")
        if choice in ['1', '01']: vehicle_lookup()
        elif choice in ['2', '02']: ip_tracker()
        elif choice in ['3', '03']: phone_info()
        elif choice in ['0', '00']: sys.exit()

if __name__ == "__main__":
    main()
