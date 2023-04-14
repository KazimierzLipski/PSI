import socket
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="Server name to listen at")
    parser.add_argument("port", help="Port number to listen at")
    args = parser.parse_args()

    name = args.name
    port = int(args.port)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((name, port))

        while True:
            data_received, client_address = s.recvfrom(1024)
            print(f"Received {len(data_received)} bytes of data from: {client_address}")
