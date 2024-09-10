#!/bin/python3

import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    diagonal1_sum = 0
    diagonal2_sum = 0
    for i in range(n):
        diagonal1_sum = diagonal1_sum + arr[i][i]
        diagonal2_sum = diagonal2_sum + arr[i][(n - 1) - i]

    return abs(diagonal1_sum - diagonal2_sum)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
