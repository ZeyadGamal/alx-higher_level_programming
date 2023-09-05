#!/usr/bin/python3
flag = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - flag)), end="")
    if flag == 0:
        flag = 32
    else:
        flag = 0
