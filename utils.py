def sum_of_digits(n):
    str_ = str(n)
    list_ = list(str_)
    int_list = map(int, list_)
    sum_ = sum(int_list)
    return sum_
