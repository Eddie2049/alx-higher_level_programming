#!/usr/bin/python3
for i in range(122, 97 - 1, -1):
    if i % 2 == 0:
        d_ = 0
    else:
        d_ = 32
    print('{}'.format(chr(i - d_)), end='')
