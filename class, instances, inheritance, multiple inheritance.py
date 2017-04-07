class Mario():
    def __init__(self, name):
        self.name = name
        print('i am ' + self.name + ' mario ')

class Shroom():
    def grow_big(self):
        print('i Grow big when i eat shroom')

class SuperMario(Mario,Shroom):
    pass

littlemario = SuperMario('kushel')
littlemario.grow_big()

