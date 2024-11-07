import argparse

import pytest

from fib import fibonacci_iterative


def test_fib_9_is_34():
    assert fibonacci_iterative(9) == 34


def test_fib_negative_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)


if __name__ == "__name__":
    parser = argparse.ArgumentParser()

    parser.add_argument('filename')  # positional argument
    parser.add_argument('-c', '--count')  # option that takes a value
    parser.add_argument('-v', '--verbose',
                        action='store_true')  # on/off flag
    parser.add_argument('nth', type=int, help="nth Fibonacci number")
    args = parser.parse_args()

    result = fibonacci_iterative(args.nth)
    print(result)
