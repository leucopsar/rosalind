# common fib: k number of offspring per pair
def fib(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1, k) + k*fib(n-2, k)


def mortal_fib(n, m):
    f = {} # mature
    d = {} # bornd
    f[0] = 0
    d[0] = 1
    f[1] = 1
    d[1] = 0
    # dynamic
    for i in range(2, n):
        d[i] = f[i-1]
        f[i] = d[i-1]+f[i-1] - (d[i-m] if i >= m else 0)
    print(d)
    print(f)
    return d[i] + f[i]


print(mortal_fib(89, 16))
