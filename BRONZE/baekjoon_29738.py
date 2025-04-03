t = int(input())
for x in range(1,t+1):
    rank = int(input())

    if rank > 4500 :
        print(f'Case #{x}: Round 1')
    elif rank > 1000 and rank <= 4500 :
        print(f'Case #{x}: Round 2')
    elif rank > 25 and rank <= 1000:
        print(f'Case #{x}: Round 3')
    elif rank <= 25 :
        print(f'Case #{x}: World Finals')