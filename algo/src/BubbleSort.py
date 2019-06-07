#!/usr/bin/python
import sys

def sort(array):
    length = len(array) - 1
    min_index = 0

for i in range(0, length):
    min_index = i
    min_value = array[min_index]

for j in range(i, length):
    if min_value > array[j + 1]:
        min_value = array[j + 1]
        min_index = j + 1

if i != min_index:
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp

def main():
    grades = [
        80,
        60,
        30,
        65,
        78,
        20,
        ]

sort(grades)
for score in grades:
    print (score, ',', end == '')
    if __name__ == '__main__':

        main()
