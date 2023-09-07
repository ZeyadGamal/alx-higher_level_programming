#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    res = 0
    for i in range(length):
        res += int(sys.argv[i + 1])
    print(res)
