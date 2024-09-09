#!/bin/python3

import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    time = s.split(":")
    if (s[-2:] == "PM") and (s[0:2] != "12"):
        return f"{int(time[0]) + 12}{s[2:-2]}"
    elif (s[-2:] == "AM") and (s[0:2] == "12"):
        return f"{s[2:-2]:0>{8}}"
    else:
        return s[:-2]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
