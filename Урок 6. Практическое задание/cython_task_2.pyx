
cpdef list compose_list():
    cdef int multiplier = 10
    cdef list returned_value = []
    cdef int index
    for index in range(500000):
        returned_value.append(index ** multiplier)
    return returned_value