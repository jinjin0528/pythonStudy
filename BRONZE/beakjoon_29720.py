import sys
input = sys.stdin.readline()

n,m,k = map(int,input())
print(max(n-(m*k),0), max(n-(m*(k-1)+1),0))