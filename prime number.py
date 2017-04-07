for num in range(3,100):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print('%d is a factor of %d*%d'%(num,i,j))
            break
    else:
        print("%d is a prime number" %(num))
