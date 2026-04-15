#Echo Server


import socket
from datetime import datetime 
port_num = int(input("Enter Port Number: \n"))


def case_switching(message):
    return message.swapcase()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '172.30.214.46' # CHANGE TO LOCAL IP
    server_socket.bind((server_ip, port_num))
    server_socket.listen(5)
    print(f"Server listening on port {port_num} (Ctrl+C to stop)")

    while True:
        client_socket, client_ip = server_socket.accept()
        print(f"Connection from {client_ip[0]}:{client_ip[1]}")
        while True:
            data = client_socket.recv(1024)
            if not data: 
                break
            message = data.decode()
            print(f"Converting the received message... \"{message}\" ")
            converted_message = case_switching(message)
            input_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = f"Message Received at {input_time}: {converted_message}"
            client_socket.sendall(response.encode())
    
        print("Client disconnected.")
        return


if __name__ == "__main__":
    main()  