def best_sales(revenue_by_day:list):

    """
    >>> best_sales([[10, 100, 400, 300], [50, 40, 200,1000], [4, 80, 12, 36]])
    [[400, 300, 100], [1000, 200, 50], [80, 36, 12]]

    """
    summa = []

    for average in revenue_by_day:
        average.sort()
        average.reverse()
        average[:3]
        summa.append(average[:3])
    return summa

