for i in range(int(input())):
    t = int(input())
    cycle = t % 25
    if cycle < 17:
        print("ONLINE")
    else:
        print("OFFLINE")