from builtins import print
import time
import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5582
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
        print(header)
        if DISCONNECT_MSG == header.rstrip():
            connected = False
        if connected:
            parts = split_HEADER(header)
            print("parts", parts)
            if check_HOST(parts, conn):
                if parts[0] == "PUT" or parts[0] == "POST":
                    length_next_chunk = int(parts[3]['Content length'])
                    body = get_PART(conn, length_next_chunk)
                    parts.append(body)
            redirect_msg(parts, conn)

    conn.close()
    print(f"[ACTIVE_CONNECTIONS] {threading.active_count()-2}")


def redirect_msg(parts, conn):
    method = parts[0]
    if method == 'GET':
        handle_GET(parts, conn)
    elif method == 'HEAD':
        handle_HEAD(parts, conn)
    elif method == 'PUT':
        handle_PUT(parts, conn)
    elif method == 'POST':
        handle_POST(parts, conn)
    else:
        stat_line = STATUS_CODE[400]
        response_body = "<html><body><h1>No valid request</h1></body></html>"
        c_length = len(response_body.encode(FORMAT))
        headers = f"DATE: {TIME}\r\nContent type: plain/text\r\nContent length: {c_length}"
        respond(conn, stat_line, headers, response_body)
        return


def handle_GET(parts, conn):
    pass


def handle_HEAD(parts, conn):
    pass


def handle_POST(parts, conn):
    pass


def handle_PUT(parts, conn):
    pass


def check_HOST(parts, conn):
    heads: dict = parts[3]
    if 'Host' not in heads.keys():
        stat_line = STATUS_CODE[400]
        response_body = "<html><body><h1>No host field given</h1></body></html>"
        c_length = len(response_body.encode(FORMAT))
        headers = f"DATE: {TIME}\r\nContent type: plain/text\r\nContent length: {c_length}"
        respond(conn, stat_line, headers, response_body)
        return False
    return True


def respond(conn, status_line, headers, msg_body=""):
    msg = status_line + "\r\n" + headers + "\r\n\r\n" + msg_body
    conn.send(msg.encode(FORMAT))
    return


def get_PART(conn, size):
    buffer = ""
    while "\r\n\r\n" not in buffer:
        buffer += conn.recv(size).decode(FORMAT)
    return buffer


def split_HEADER(msg):
    # hier moet nog een big check komen
    request = ''.join((line + '\n') for line in msg.splitlines())
    request_head = request.splitlines()  # List of request and headers
    print("request_head", request_head)
    request_line = request_head[0]
    method, uri, http = request_line.split(' ', 3)
    headers = {}
    for head in request_head[1:len(request_head)-1]:
        elem = head.split(": ", 1)
        headers[elem[0]] = elem[1]
    return [method, uri, http, headers]


if __name__ == "__main__":
    main()


# def handle_msg(msg: str, conn):
#     request = normalize_msg(msg)
#     try:
#         request_head, body = request.split('\n\n', 1)
#         print("request head:", request_head, "body", body)
#     except:
#         status_line: str = STATUS_CODE[400]
#         response_body = "<html><body><h1>No valid method</h1></body></html>"
#         header = "Date: " + TIME + "\r\n" + "Content type: " + "plain/text" + \
#             + "\r\n" + "Content length: "  # + \
#         # str(len(response_body.encode(FORMAT)))
#         send_RESPONSE(conn, status_line, header, response_body)
#     request_head = request_head.splitlines()  # List of request and headers
#     request_line = request_head[0]
#     method, uri, http = request_line.split(' ', 3)
#     headers = {}
#     for head in request_head[1:]:
#         elem = head.split(": ", 1)
#         headers[elem[0]] = elem[1]
#         print(method, uri, http, headers, "body", body)
#     return [method, uri, http, headers, body]


# def handle_GET(msg, conn):
#     check_HOST_HEADER(msg, conn)


# def handle_HEAD(msg, conn):
#     check_HOST_HEADER(msg, conn)


# def handle_PUT(msg, conn):
#     check_HOST_HEADER(msg, conn)
#     msg_parts = handle_msg(msg, conn)
#     path = os.path.dirname(os.path.abspath(__file__))
#     file_name = msg_parts[1]
#     with open(os.path.join(path, file_name), 'wb') as newfile:
#         newfile.write(msg_parts[4].encode(FORMAT))
#     status_line = "HTTP/1.1 " + STATUS_CODE[200] + "\r\n"
#     response_body = "<html><body><h1>The file was created.</h1></body></html>"
#     headers: str = "Date: " + TIME + "\r\n" + "Content type: " + "plain/text" + \
#         + "\r\n" + "Content length: " + len(response_body.encode(FORMAT))
#     send_RESPONSE(conn, status_line, headers, response_body)


# def handle_POST(msg, conn):
#     check_HOST_HEADER(msg, conn)


# def check_HOST_HEADER(msg, conn):
#     headers = handle_msg(msg, conn)[3]
#     if 'Host' not in headers:
#         status_line: str = STATUS_CODE[400]
#         response_body = "<html><body><h1>No host header in request</h1></body></html>"
#         header: str = "Date: " + TIME + "\r\n" + "Content type: " + "plain/text" + \
#             + "\r\n" + "Content length: " + len(response_body.encode(FORMAT))
#         send_RESPONSE(conn, status_line, header, response_body)


# def send_RESPONSE(conn, status_line: str, headers: str, body: str = ""):
#     msg = status_line + headers + "\r\n\r\n" + body
#     conn.send(msg.encode(FORMAT))
