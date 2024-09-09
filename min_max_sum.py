#!/bin/python3

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.


def miniMaxSum(arr):
    inc = sorted(arr)
    dec = sorted(arr, reverse=True)

    print(str(sum(inc[0:4])) + " " + str(sum(dec[0:4])))


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
