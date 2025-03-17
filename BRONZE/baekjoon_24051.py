import sys
def insertion_sort_kth_save(n, k, arr):
    cnt = 0  # 저장 횟수 카운트

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 저장 발생
            cnt += 1
            if cnt == k:
                print(arr[j])
                return
            j -= 1

        if arr[j + 1] != key:  # 제자리 정렬 제외
            cnt += 1
            arr[j + 1] = key

        if cnt == k:
            print(key)
            return

    print(-1)  # 저장 횟수가 K보다 작은 경우

input = sys.stdin.read
data = input().split()
n, k = map(int, data[:2])
arr = list(map(int, data[2:]))

insertion_sort_kth_save(n, k, arr)
