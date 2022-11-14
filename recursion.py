
def fact(n):
    """_summary_    : Finds Factorial of a number

    Args:
        n (_type_): _description_   : Number

    Returns:
        _type_: _description_  : Factorial of the number
    """
    if n == 0:
        return 1
    return n * fact(n-1)


def sum_n(n):
    if n == 0:
        return 0
    small_output = sum_n(n-1)
    output = small_output + n
    return output


n = int(input())
print(f"factorial is :", fact(n))
print(f"sum is :", sum_n(n))
