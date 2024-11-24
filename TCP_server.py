from socket import *
import time

def main():
    print("Starting TCP Server...")

    host_local = "127.0.0.1"
    port_local = 50000
    buffer_size = 1024

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host_local, port_local))
    server_socket.listen(1)

    print("TCP server starts listening (Waiting for messages)")

    while True:
        conn, address = server_socket.accept()
        print("Connected to:", address)

        for _ in range(10):
            message = conn.recv(buffer_size).decode()
            if not message:
                break
            print("Message from client:", message)

        response_message = f"Messages processed. Received at {time.asctime()}"
        conn.sendall(response_message.encode())
        conn.close()

if __name__ == "__main__":
    main()
