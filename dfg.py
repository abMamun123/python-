def find_min_removals(a):
    freq = {}
    removals = 0

    for x in a:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1

    for x in freq:
        if freq[x] > x:
            removals += freq[x] - x
        elif freq[x] < x:
            removals += freq[x]

    return removals

n = int(input())
a = list(map(int, input().split()))

min_removals = find_min_removals(a)
print(min_removals)
