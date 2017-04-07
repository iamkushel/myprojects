import threading

class Enemy(threading.Thread):
    def run(self):
       for _ in range(10):
            print(threading.currentThread().getName())

x = Enemy()
y = Enemy(name ='attacking enemy2')
x.start()
y.start()
