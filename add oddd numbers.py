class Maths:
    n =int(input("enter the value of n"))

    def addtion(self, sum):
        for a in range(1, self.n):
            if a%2 == 0:
                pass
            elif a%2 == 1:
                sum = a + int(sum)
        print(sum)
add = Maths()
add.addtion(0)

