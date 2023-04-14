import socket
import argparse
from random import choices
import string
from time import sleep
import math

def getMiddle(lower: int, upper: int):
    return math.floor((lower+upper)/2)

def generate_data(size):
    rand_str = ''.join(choices(string.ascii_letters, k=size))
    return str.encode(rand_str)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("server_name", help="Server's name")
    parser.add_argument("server_port", help="Server's port")

    args = parser.parse_args()

    server_name = args.server_name
    server_port = int(args.server_port)

    lower = 1
    upper = 100000
    lastMiddle = getMiddle(lower, upper)
    middle = -1

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while lastMiddle != middle:
            lastMiddle = middle
            middle = getMiddle(lower, upper)
            data = generate_data(middle)
            try:
                print(f"Sending {len(data)} bytes of data...   ", end="")
                s.sendto(data, (server_name, server_port))
                print("Sent")
                lower = middle
            except OSError:
                print("Too big!")
                upper = middle

            sleep(0.5)

    print("Maksymalny datagram jaki jest obsługiwany to " + middle + " bajtów")