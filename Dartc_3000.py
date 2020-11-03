def kadane(a, K):
    n = len(a)
    max_so_far = 0
    if a[K] < 0:
        max_so_far = max(a)
    max_ending_here = 0
    for i in range(0, n):
        if K >= 0 and K <= i:
            max_ending_here = 0
        else:
            max_ending_here = max_ending_here + a[i]
        if (max_ending_here < 0):
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

def maxCircularSum(a, K):
    n = len(a)
    max_kadane = kadane(a, K)
    max_wrap = 0
    for i in range(0, n):
        if K >= 0 and K == i:
            max_wrap = 0
        else:
            max_wrap += a[i]
            a[i] = -a[i]

    if K > 0:
        max_wrap = max_wrap + max_kadane
    else:
        max_wrap = max_wrap + kadane(a, K)

    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane

X = int(input())

for i in range(X):

    N, K = map(int, input().split())

    a = [int(i) for i in (input().split())]

    print(maxCircularSum(a, K))
