def marks(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    return avg
print(marks([23, 23, 2, 38, 96, 42, 83]))

date, *time, month = (22, '11:30', '11:45', '12:30', 'feb')

print(time)
