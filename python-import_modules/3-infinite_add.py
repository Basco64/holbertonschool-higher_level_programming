#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0

    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])

    print("{}".format(result))
