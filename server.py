import socket
import pyautogui
from pynput.keyboard import Key, Controller
# Server configuration
HOST = '192.168.0.103'  # Use your server's IP address
PORT = 12345

# Initialize server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Server listening on", HOST, PORT)


# Initialize keyboard controller
keyboard = Controller()

# Accept client connection
client_socket, addr = server_socket.accept()
print("Connected by", addr)

while True:
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        # Split received data into command and parameters
        command_parts = data.split(',')
        command = command_parts[0]

        if command == 'move':
            x, y = map(int, command_parts[1:])
            pyautogui.moveRel(x, y)
        elif command == 'click':
            button = command_parts[1]
            pyautogui.click(button=button)
        elif command.startswith('scroll'):
            lines = int(command_parts[1])
            pyautogui.scroll(lines)
        elif command.startswith('key'):
            key = command_parts[1]
            if key == 'left':
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            elif key == 'right':
                keyboard.press(Key.right)
                keyboard.release(Key.right)
        elif command == 'exit':
            break

    except Exception as e:
        print("Error:", e)

# Close sockets
client_socket.close()
server_socket.close()
print("Server closed")
