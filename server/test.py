from builtins import print
import time
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 8088
ADDR = (IP, PORT)
SIZE = 1
FORMAT = "utf-8"
DISCONNECT_MSG = "DISCONNECT!"
STATUS_CODE = {200: "200 OK", 404: "404 Not Found",
               400: "Bad Request", 500: "Server Error", 304: "Not Modified"}
TIME = time.strftime("%a, %d %b %Y %I:%M:%S %Z", time.gmtime())


def main():
    print(f"[STARTING] {IP, PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] ON {IP} : {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE_CONNECTIONS] {threading.active_count()-1}")


def handle_client(conn, addr):
    print(f"[NEW_CONNECTION] {addr} connected.")
    connected = True
    while connected:
        header = get_PART(conn, SIZE)
        if DISCONNECT_MSG in header:
            connected = False
        _header = split_HEADER(header)
        print(f"[{addr}] HEADER:{header}")  # BODY: {rest}")  # debugging
        print("splitted header:", split_HEADER(_header))
        # msg = f"msg received: {_header}\r\n rest: {rest}"  # debugging puspose
        # conn.send(msg.encode(FORMAT))  # debugging purpose
    conn.close()
    print(f"[ACTIVE_CONNECTIONS] {threading.active_count()-2}")


def get_PART(conn, size):
    buffer = ""
    while "\r\n\r\n" not in buffer:
        print(conn.recv(size))
        print(conn.recv(size).decode(FORMAT))
        buffer += conn.recv(size).rstrip().decode(FORMAT)
    return buffer


def split_HEADER(msg):
    # hier moet nog een big check komen
    request = ''.join((line + '\n') for line in msg.splitlines())
    request_head, body = request.split('\n\n', 1)
    request_head = request_head.splitlines()  # List of request and headers
    request_line = request_head[0]
    method, uri, http = request_line.split(' ', 3)
    headers = {}
    for head in request_head[1:]:
        elem = head.split(": ", 1)
        headers[elem[0]] = elem[1]
        print(method, uri, http, headers, "body", body)
    return [method, uri, http, headers, body]


main()
