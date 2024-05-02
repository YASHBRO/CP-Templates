from __future__ import division, print_function
import os
import sys
from collections import *
from math import *
from io import BytesIO, IOBase
if sys.version_info[0] < 3:
    from builtins import xrange as range
    from future.builtins import ascii, filter, hex, map, oct, zip


def input(): return sys.stdin.readline().rstrip("\r\n")
def int_in(): return(int(input()))
def list_in(): return(list(map(int, input().split())))
def map_in(func=int, sep=None): return(map(func, input().split(sep)))


def main():
    pass


# region fastio
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


# endregion


# ------------Stack------------ #
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# ------------Queue------------ #
class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


# ------------Prime DP Table------------ #
def primeTableDP(n):
    primeTable = [True] * (n + 1)
    p = 2
    primeTable[0], primeTable[1] = False, False
    while p * p <= n:
        if primeTable[p]:
            for i in range(p * p, n + 1, p):
                primeTable[i] = False
        p += 1
    return primeTable


# ------------Get Divisors/Factors------------ #
def getDivisor(n, maxDivs=0, include_1=True):
    res = []
    i = 1 if include_1 else 2
    while (i * i < n):
        if (n % i == 0):
            res.append(i)
        if maxDivs > 0 and len(res) >= maxDivs:
            return res
        i += 1
    for i in range(int(sqrt(n)), 0, -1):
        if (n % i == 0):
            res.append(n//i)
        if maxDivs > 0 and len(res) >= maxDivs:
            return res


# ------------Check Prime------------ #
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# ------------Tree in Dictionary------------ #
def dictTree(pNode):
    n = len(pNode)+1
    tree = dict()
    for i in range(n):
        tree[i+1] = []
    for i in range(n - 1):
        tree[pNode[i]] += [i + 2]
    return tree


# ------------Frequency of elements------------ #
def frequencyDict(arr):
    return Counter(arr).most_common()


# ------------Binary Search------------ #
def binarySearch(arr, val):
    l, r = 0, len(arr)
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# ------------Lower Bound------------ #
def lowerBound(arr, val):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= val:
            high = mid - 1
        else:
            low = mid + 1

    return low


# ------------Upper Bound------------ #
def upperBound(arr, val):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return low


# ------------Shift Character------------ #
def shift_char(string, index, dir='l', places=1):
    temp = string[index]
    string = string[:index]+string[index+1:]
    if dir == 'l':
        return (string[:index-places]+string[index]+string[index-places:])
    else:
        return (string[:index+places]+string[index]+string[index+places:])


if __name__ == "__main__":
    main()
