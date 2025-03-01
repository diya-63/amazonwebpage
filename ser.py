import socket

def start_server():
    PORT = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(5)
    print(f"Server listening on port {PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Client connected: {client_address[0]}")
        client_message = client_socket.recv(1024).decode()
        print(f"Received from client: {client_message}")
        
        # Respond to the client
        response = "Server says: Hello, Client!"
        client_socket.send(response.encode())
        
        client_socket.close()

if __name__ == "__main__":
    start_server()
