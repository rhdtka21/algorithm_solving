import sys
read = sys.stdin.readline

GAN = "0123456789"
JI = "ABCDEFGHIJKL"

def gabja(N):
    year = abs(N - 4) % 60
    i = year
    gan = i % 10
    ji = i % 12
    return JI[ji]+GAN[gan]

N = int(read())
print(gabja(N))