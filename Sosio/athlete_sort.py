N, M = map(int, input().split())
arr = [input() for _ in range(N)]
K = int(input())

for row in sorted(arr, key=lambda row: int(row.split()[K])):
    print(row)
