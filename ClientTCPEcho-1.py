#Echo Client

import socket


def main():
    server_ip = input("Enter server IP Address: \n")
    port_num = int(input("Enter Port Number: \n"))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    client_ip = socket.gethostbyname(hostname)
    client_socket.connect((server_ip, port_num))

    print(f"Connecting to server using client's IP \"{client_ip}\" and TCP")
    print(f"Connected to server at {server_ip}:{port_num}")
    print("Type a message to send or 'DONE' to quit: ")

    while True:
        message = input("Client: Enter message to send to Server: \n")
        if message == "DONE":
            print("Quitting, connection closed.")
            client_socket.close()
            break

        client_socket.sendall(str.encode(message))
        recvData = client_socket.recv(1024)
        recvMessage = recvData.decode()
        print(recvMessage)


if __name__ == "__main__":
    main()

