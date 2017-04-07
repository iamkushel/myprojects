class Enemy:
    life = 100
    def __init__(self, x):
        print(' captain\'s Message We will not give, we will fight of our nation, for our children, for our women till the last breath')
        self.guns = x
    def attack(self):
        print('parahparaaah, Yeeehaaa')
        print('we are being attacked use' + self.guns)
        self.life -= 5
        if self.life >= 60:
            print('We can do it on our own')
        else:
            print('Call the Captain')
    def remaining_life(self):
        if self.life <= 0:
            print('Aaaaaaaaaaaaaaaaa, thadddd!!! RIP Solider')
        else:
            print(self.life)

enemy1 = Enemy('snipper')
enemy1.attack()
enemy1.remaining_life()




