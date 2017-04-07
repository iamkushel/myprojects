#First way of writing an exception
while True:
    try:
        a = int(input('enter your student id'))
        print(a*2)
        break
    except ValueError:
        print('Student id must contain only numbers, Please try again')
    finally:
        print('Have a good one!!!!')
#second way of writing exception

try:
    a = int(input('enter your student id'))
    print(2/a)

except ValueError:
    print('Student id must contain only numbers, Please try again')
except:
    exit()
else:
    print('this the answer')
finally:
    print('Have a good one!!!!')
