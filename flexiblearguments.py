def mul_num(*args):
    total = 1;
    for a in args:
        total *= a
    print(total)


mul_num(5,2)
mul_num(5,2,4)

numbers = [5,4,3,2,1]
mul_num(*numbers)
