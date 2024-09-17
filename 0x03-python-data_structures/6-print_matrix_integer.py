#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix):
        for i in matrix:
            for j, elem in enumerate(i):
                # print each elem with a space,
                # except the last one
                if (j < len(i) - 1):
                    print("{:d}".format(elem), end=" ")
                else:
                    print("{:d}".format(elem), end="")
            # move to the next line after each row.
            print()
