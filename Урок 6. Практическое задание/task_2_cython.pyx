cpdef int sieve_cython(int n):
    cdef int m
    cdef list a = []
    cdef int i, j
    cdef int prime_num 
    m = n * 10
    a = [i for i in range(m + 1)]
    a[1] = 0
    i = 2

    while i <= m:
        if a[i] != 0:
            j = i + i
            while j <= m:
                a[j] = 0
                j = j + i
        i += 1

    a = [i for i in a if i != 0]
    prime_num = a[n - 1]
	
    return prime_num

