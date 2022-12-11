# Name: RAJESH KUMAR YADAV
# Sap id: 500084908
# Roll no: R2142201739
# Batch: 2(H)
# Course: Container Orchestration and Infrastructure Automation
# Program: BTECH CSE & Spl. CC&VT


import socket
import os
import random
import hashlib


def get_checksum(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        res = hashlib.sha256(bytes).hexdigest()
    return res

def main():
    
    try:
        os.mkdir(os.path.join("./","serverdata"))
    except:
        pass

    
    f = open("./serverdata/data.txt", "w")
    for i in range(20):
        randomlist = random.randint(1,100)
        f.write(str(randomlist) + '\n')
    f.close()
    
    host = socket.gethostname()
    try:
        port = os.environ["PORT"]
    except:
        port = 8081
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    connection = server_socket.accept()[0]

    
    file_to_read = open("./serverdata/data.txt", "rb")
    data = file_to_read.read(1024)
    while data:
        connection.send(data)
        data = file_to_read.read(1024)
    file_to_read.close()

    
    checkSum = get_checksum("./serverdata/data.txt")
    connection.send(checkSum.encode())
    
    
    connection.close()

if __name__ == '__main__':
    main()
