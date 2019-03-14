def best_sales(revenue_by_day:list):


    """
    >>> best_sales([[10, 100, 400, 300, 0, 0, 0], [50, 40, 200, 1000, 150, 0, 46], [4, 80, 12, 36, 0, 15, 16]])
    [[100, 300, 400], [150, 200, 1000], [16, 36, 80]]

    """
    summa = []

    for average in revenue_by_day:
        average.sort()
        summa.append(average[4:])
    return summa

