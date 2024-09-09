#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    zeros = 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeros += 1

    print(positives / len(arr))
    print(negatives / len(arr))
    print(zeros / len(arr))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
