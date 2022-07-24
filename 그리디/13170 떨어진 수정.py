import sys
input = sys.stdin.readline

n, k, p, w = map(int, input().split())
print((p + w -1) // w)