n = int(input())
arr = list(map(int, input().split()))

x = 0
for num in arr:
    if num % 2 != 0:
        print(0)
        break
else:
    while True:
        for i in range(n):
            if arr[i] % 2 != 0:
                print(x)
                break
            else:
                arr[i] = arr[i] // 2
        else:
            x += 1
            continue
        break
