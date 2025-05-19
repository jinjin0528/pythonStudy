while True:
    line = input()
    if line == "0":
        break

    nums = list(map(int, line.split()))
    N, data = nums[0], nums[1:]

    result = []
    prev = None
    for num in data:
        if num != prev:
            result.append(str(num))
        prev = num

    print(' '.join(result) + ' $')