#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_ = len(sys.argv) - 1
    if (num_ < 1):
        print("{} arguments.".format(num_))
    elif (num_ == 1):
        print("{} argument:".format(num_))
    else:
        print("{} arguments:".format(num_))
    for i in range(num_):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
