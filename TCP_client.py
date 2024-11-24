from socket import *
import time

def main():
    server_host = '127.0.0.1'
    server_port = 50000
    buffer_size = 1024
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    message = "Lila"
    start_time = time.time()

    try:
        for _ in range(10):
            client_socket.sendall(message.encode())

            response = client_socket.recv(buffer_size)
            print("Response from server:", response.decode())

            total_bytes = len(message.encode())
            transmission_time = time.time() - start_time
            throughput = total_bytes / transmission_time if transmission_time > 0 else 0
            print(f"Throughput: {throughput:.2f} bytes/second")

        client_socket.close()
    except Exception as e:
        print(f"An error happened: {e}")

if __name__ == "__main__":
    main()
