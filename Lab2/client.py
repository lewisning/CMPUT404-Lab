import socket


def main():
    # Initialize the client
    new_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Create a connection
    url = 'www.google.com'
    new_client.connect((url, 80))
    new_client.send("GET / HTTP/1.1\r\n".encode("utf-8"))
    new_client.send(("Host: " + url + "\r\n").encode("utf-8"))
    new_client.send("\n".encode("utf-8"))

    # Get the data from web with size 4096 bytes
    while True:
        data = new_client.recv(4096)
        if len(data) > 0:
            print(data)
        else:
            break


main()
