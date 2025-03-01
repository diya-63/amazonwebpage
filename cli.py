import socket

def start_client():
    SERVER_IP = '127.0.0.1'  # Change to server's IP if needed
    SERVER_PORT = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    message = input("Enter a message to send to the server: ")
    client_socket.send(message.encode())
    print(f"Sent to server: {message}")
    
    server_response = client_socket.recv(1024).decode()
    print(f"Received from server: {server_response}")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
