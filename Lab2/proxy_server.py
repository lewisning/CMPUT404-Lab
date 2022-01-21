#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


def remote_ip(host):
    print(f"Getting IP for {host}")
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Could not find the host address!")
        sys.exit()
    print(f"Remote IP address of {host} is {ip}")
    return ip


def main():
    # Connect to Google
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_s:
        # Set up a proxy server
        proxy_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind socket to address
        proxy_s.bind((HOST, PORT))
        # set to listening mode
        proxy_s.listen(1)
        print("Start Proxy Client connection")

        # continuously listen for connections
        while True:
            #connect proxy start
            conn, addr = proxy_s.accept()
            print("Connect by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_e:
                print("Connecting to Google")
                ip = remote_ip(host)

                #connect proxy_end
                proxy_e.connect((ip, port))

                #send data
                send_full_data = conn.recv(BUFFER_SIZE)
                print(f'Sendinf recieved data {send_full_data} to Google')
                proxy_e.sendall(send_full_data)

                # Shut down
                proxy_e.shutdown(socket.SHUT_WR)

                back_data = proxy_e.recv(BUFFER_SIZE)
                conn.send(back_data)

            conn.close()


if __name__ == "__main__":
    main()
