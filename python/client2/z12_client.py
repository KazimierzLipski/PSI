import socket
import argparse
from random import choices
import string
from time import sleep

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

    data_sizes = [1, 100, 300, 500, 5000, 25000, 32500, 40000, 59000, 69000, 65507, 65508]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for data_size in data_sizes:
            data = generate_data(data_size)
            try:
                print(f"Sending {len(data)} bytes of data...   ", end="")
                s.sendto(data, (server_name, server_port))
                print("Sent")
            except OSError:
                print("Too big!")

            sleep(0.5)