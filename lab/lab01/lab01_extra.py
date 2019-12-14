"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    fac = 1
    depth = n - k
    while n > depth:
        fac = fac * n
        n = n - 1
    return fac

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    previousIs8 = False
    while n > 0:
        rightDigit = n % 10
        if rightDigit == 8 and previousIs8:
            return True
        elif rightDigit == 8:
            previousIs8 = True
        else:
            previousIs8 = False
        n = n // 10
    return False

