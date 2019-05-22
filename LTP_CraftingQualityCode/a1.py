def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(0)
    0
    >>> num_buses(50)
    1
    """

    if n % 50 == 0:
        return n // 50
    else:
        return n // 50 + 1

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([0.19, -0.05, -0.02, 0.04, -0.07, 0, 0.06, -0.11])
    (0.29, -0.25)
    """
    gains = 0
    losses = 0

    for n in price_changes:
        if n > 0:
            gains += n
        elif n < 0:
            losses += n

    return round(gains, 2), round(losses, 2)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    >>> nums = [1, 2, 3, 4, 5, 6, 'A', 'B', 'C']
    >>> swap_k(nums, 3)
    >>> nums
    ['A', 'B', 'C', 4, 5, 6, 1, 2, 3]
    """

    first_k_items = L[:len(range(k))]

    for i in range(k):
        L[i] = L[-len(range(k)) + i]
        L[-len(range(k)) + i] = first_k_items[-len(range(k)) + i]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
