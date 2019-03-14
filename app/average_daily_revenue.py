def averages_daily(revenue_by_day):

    """
    >>> averages_daily([[10], [5, 10], [4, 8, 12]])
    10.0

    >>> averages_daily([[10], [5, 10, 15], [4, 8, 12, 16, 20, 24, 28]])
    16.0

    >>> averages_daily([[5, 10, 15, 20, 25, 30, 35], [10, 20, 30, 40, 50, 60, 70], [4, 8, 12, 16, 20, 24, 28]])
    40.0
    """
    summas = []  # empty list to save the averages daily revenue

    for average in revenue_by_day:
        result = 0
        for i in average :
            result += i
            av = result/len(average)
        summas.append(av)
    max_value = max(summas)
    return  max_value
