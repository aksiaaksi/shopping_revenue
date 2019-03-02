def best_everyday_revenue(revenue_by_day):

    """
    >>> best_everyday_revenue([[17], [5, 10], [4, 16, 12]])
    4

    >>> best_everyday_revenue([[10], [5, 10, 15], [6, 8, 12, 16, 20, 24, 28]])
    5
    """

    summa = []

    for revenue in revenue_by_day:
        for i in revenue:
            min_value = min(revenue)
        summa.append(min_value)
    min_value = min(summa)

    return min_value