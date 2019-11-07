def sumrange(rangemax):
    thesum = 0
    for i in range(rangemax):
        thesum += i

    return thesum

def sumrange_fast(int rangemax):
    cdef int thesum = 0
    cdef int i

    for i in range(rangemax):
        thesum += i

    return thesum
