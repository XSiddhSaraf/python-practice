
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def sum_n(n):
    if n == 0:
        return 0
    smallOutput = sum_n(n-1)
    output = smallOutput + n
    return output


n = int(input())
print(f"factorial is :", fact(n))
print(f"sum is :", sum_n(n))
