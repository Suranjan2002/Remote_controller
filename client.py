import socket
import time

# Server configuration
HOST = ''  # Replace with server's IP address
PORT = 0
def set_parameters(host,port):
    global HOST, PORT
    HOST = host
    PORT = int(port)


client_socket = ''
def connect_socket():
    # Initialize client socket
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return 'Connected to server'
    #print("Connected to server")

def perform_operation(command):
    global client_socket
    try:
        #command = input("Enter command (left, right, scroll, left_arrow, right_arrow, exit): ")
        if command == 'exit':
            client_socket.sendall(command.encode())
            client_socket.close()
            print("Client Closed")
        elif command == 'left' or command == 'right':
            client_socket.sendall(f'click,{command}'.encode())
        elif command.startswith('scroll'):
            lines = int(command.split(',')[1])
            data = f"scroll,{lines}"
            client_socket.sendall(data.encode())
        elif command == 'left_arrow':
            client_socket.sendall('key,left'.encode())
        elif command == 'right_arrow':
            client_socket.sendall('key,right'.encode())
        else:
            print("Invalid command")

    except Exception as e:
        print("Error:", e)

    
''' set_parameters('192.168.0.103',12345)
connect_socket()

while True:
    command = input("Enter command (left, right, scroll, left_arrow, right_arrow, exit): ")
    perform_operation(command) '''

