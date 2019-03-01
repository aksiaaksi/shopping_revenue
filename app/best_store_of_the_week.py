def total_revenue(revenue_by_day):

    """
    >>> total_revenue([[10], [5, 10], [4, 8, 12]])
    24

    >>> total_revenue([[5, 10, 15, 20, 25, 30, 35], [10, 20, 30, 40, 50, 60, 70], [4, 8, 12, 16, 20, 24, 28]])
    280

    >>> total_revenue([[],[1,2,3]])
    6
    """

    summas = [] #empty list to save the amount of revenue for the week

    for summa in revenue_by_day:
        rezult = 0
        for i in summa:
            rezult += i
        summas.append(rezult)

    max_value = max(summas)
    return  max_value

