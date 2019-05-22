def averages(grades):
    ''' (list of list of number) -> list of float

    Return a new list in which each item is the average of the
    grades in the inner list at the corresponding position.

    >>> averages([[70, 75, 80], [70, 80, 90, 100], [80, 100]])
    [75.0, 85.0, 90.0]
    '''

    averages = []

    for assn_list in grades:
        # Calculate the average of class and append it to averages.

        total = 0
        
        for assignment in assn_list:
            total += assignment
            
        averages.append(total / len(assn_list))

    return averages
