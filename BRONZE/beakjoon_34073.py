def main():
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    words = input().strip().split()
    # 각 단어 끝에 DORO를 붙이고 공백으로 연결
    result = " ".join(word + "DORO" for word in words)
    print(result)

if __name__ == "__main__":
    main()