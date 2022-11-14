li = input().split()
x = int(li[0])
n = int(li[1])


def raisePow(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    return x * raisePow(x, n-1)


print(raisePow(x, n))
