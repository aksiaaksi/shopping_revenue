# averages = [[17], [5, 10], [4, 16, 12]]
# a = []
# for average in averages:
#     for i in average:
#         max_value = max(average)
#     a.append(max_value)
# print(a)
# max_value = max(a)
# print (max_value)

def best_everyday_revenue(revenue_by_day):

    """
    >>> best_everyday_revenue([[17], [5, 10], [4, 16, 12]])
    17

    >>> best_everyday_revenue([[10], [5, 10, 15, 30], [4, 8, 12, 16, 20, 24, 28]])
    30
    """

    summa = []

    for revenue in revenue_by_day:
        for i in revenue:
            max_value = max(revenue)
        summa.append(max_value)
    max_value = max(summa)

    return max_value


