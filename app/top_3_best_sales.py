def best_sales(revenue_by_day:list):


    """
    >>> best_sales([[10, 100, 400, 300, 0, 0, 0], [50, 40, 200, 1000, 150, 0, 46], [4, 80, 12, 36, 0, 15, 16]])
    [[400, 300, 100], [1000, 200, 150], [80, 36, 16]]

    """
    summa = []

    for average in revenue_by_day:
        average.sort(reverse = True)
        summa.append(average[:3])
    return summa

