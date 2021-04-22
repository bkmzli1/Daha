import socket
import json


def connect(MESSAGE):
    TCP_IP = 'localhost'
    TCP_PORT = 80
    BUFFER_SIZE = 1024
    # note the outer ' around the message

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE.encode())
    print("sent data")
    dataClear = s.recv(BUFFER_SIZE).decode()
    print("recieved")

    s.close()
    try:
        print(dataClear)
        data = json.loads(dataClear)[0]
        print(data)
    except Exception:
        print("json error")
        data = json.loads("[]")
    return data


def remove_char(s):
    s = s.replace('\n', '')
    s = s.replace(' ', '')
    s = s.replace('[', '')
    s = s.replace(']', '')
    return s;
