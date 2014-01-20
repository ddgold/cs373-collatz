# -------
# imports
# -------

import sys

# ----
# cash
# ----
cash = [0] * 100000

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    for s in r :
        yield map(int, s.split())
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval ((i, j)) :
    """
i is the beginning of the range, inclusive
j is the end of the range, inclusive
return the max cycle length in the range [i, j]
"""
    assert i > 0
    assert j > 0
    if i > j :
        temp = i
        i = j
        j = temp
    assert i <= j

    if i < j / 2 :
        i = j / 2

    v = 0
    for n in range(i, j + 1) :
        l = collatz_cycle(n)
        if l > v :
            v = l
    assert v > 0
    return v

# -------------
# collatz_cycle
# -------------

def collatz_cycle (n) :
    """
    n is the number for which cycle length is calculated
    return the cycle length for n
    """
    global cash
    assert n > 0
    if (n < 100000) and (cash[n] != 0) :
        return cash[n]
    else:
        if n == 1 :         #Base Case
            return 1
        elif n % 2 == 0 :   #Even
            l = 1 + collatz_cycle (n >> 1)
        else :              #Odd
            l = 2 + collatz_cycle (n + (n >> 1) + 1)
        if n < 100000 :
            cash[n] = l
        return l

# -------------
# collatz_print
# -------------
def collatz_print (w, (i, j), v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
