def even_or_odd(lst) -> tuple:
    even_numb = []
    odd_numb = []
    for numb in lst:
        if numb % 2 == 0:
            even_numb.append(numb)
        elif numb % 2 == 1:
            odd_numb.append(numb)
    return (even_numb, odd_numb)


assert even_or_odd([1, 2, 3, 4, 5]) == ([2, 4], [1, 3, 5])
assert even_or_odd([45, 44, 102, 1045]) == ([44, 102], [45, 1045])
assert even_or_odd([1, 3, 5, 7]) == ([], [1, 3, 5, 7])
assert even_or_odd([1, 4.1, 2.2, 2.5])== ([], [1])
