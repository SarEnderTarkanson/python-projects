import socket
from threading import Thread

host = "localhost"
port = 8080

clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))


def accept_clients_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, "Has connected")
        client_conn.send("Welcome to the chatroom. Please type your name to continue.".encode("utf8"))
        addresses[client_conn] = client_address

if __name__ == "__main__":
    sock.listen(5)
    print("the server is running and is listening to clients' requests.")

    t1 = Thread(target=accept_clients_connections)
    t1.start()
    t1.join()
