import socket

host = "localhost"
port = 8080

clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))

if __name__=="__main__":
    sock.listen(5)
    print("the server is running and is listening to clients' requests.")