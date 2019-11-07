#!/bin/python3

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

a_points = 0
b_points = 0

for n in range(0,3):
    if a[n] > b[n]:
        a_points += 1
    if a[n] < b[n]:
        b_points += 1

print(a_points, b_points)
