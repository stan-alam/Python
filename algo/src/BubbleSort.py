#!/usr/bin/python

import sys

def sort(array):
    length = len(array)
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            if array[j] > array[ j + 1 ]:
                tag = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tag
def main():
    grades = [85, 90, 65, 70, 92, 97]

    sort(grades)

    for grade in grades:
        print(grade, ", ", end = "")

if __name__ == "__main__":
    main()
