from linecache import cache

cache = {}


def fibonacci_iterative(n: int) -> int:
    """
  Computes the n-th Fibonacci number.
    :param n: n-th: Fibonacci number.
    :return: The n-th Fibonacci number.
    """
    # Todo: implement

    if n < 0:
        raise ValueError("n must be greater than or equal to zero")
    if n < 2:
        return n

    if n in cache:
        return cache[n]


nth = fibonacci_iterative(n - 1) + fibonacci_iterative(n - 2)

cache[n] = nth

return nth

n1 = 1
n0 = 0
result = 0

for _ in range(n - 1):
    nth = n0 + n1
    n0 = n1
    n1 = nth
return nth

if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    result = fibonacci_iterative(9)
    print(result)
