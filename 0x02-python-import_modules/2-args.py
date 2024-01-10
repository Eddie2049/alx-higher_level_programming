#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_ = len(sys.argv) - 1
    if num_ == 0:
        print("0 arguments.")
    elif num_ == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_))
    for i in range(num_):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
