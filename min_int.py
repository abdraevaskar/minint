list_ = input('Enter new list of numbers: ').split(',')
list_int = list(map(int, list_))
def min_int():
    s = []
    for i in list_int:
        if i + 1 not in list_int and i >= 0:
            s.append(i+1)
            return min(s)
        elif i < 0:
            return '1'
print(f'The minimal positive integer out of list is {min_int()}')