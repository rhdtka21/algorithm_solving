# [파이썬 | BOJ | 19532] 수학은 비대면강의입니다
import sys
read = sys.stdin.readline

a, b, c, d, e, f = map(int, read().split())

x = (c*e - b*f) // (a*e - b*d)
y = (c*d - a*f) // (b*d - a*e)

print(x, y)