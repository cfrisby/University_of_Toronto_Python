def calculate_average(asn_grades):
    ''' (list of list of [str, number]) -> float

    Return the average of the grades is asn_grades.

    >>> calculate_average([['A1', 80], ['A2', 90]])
    85.0
    '''

    sum_grades = 0

    for item in asn_grades:
        sum_grades += item[1]

    return sum_grades / len(asn_grades)
