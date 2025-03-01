a,b = map(int, input().split())
c,d = map(int, input().split())

start = min(a,c)
end = max(b,d)

double = end-start

if b<c or d<a:
    double = (b-a)+(d-c)
print(double)