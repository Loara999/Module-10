import threading
import time


class Knight(threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies:
            time.sleep(1)
            self.enemies -= self.power
            days += 1
            if self.enemies > 0:
                print(f'{self.name} сражается {days} день, осталось {self.enemies} воинов.')
            else:
                print(f'{self.name} одержал победу спустя {days} дней.')

knight1 = Knight('Владимир', 10)
knight2 = Knight('Александр', 20)
knight1.start()
knight2.start()
knight1.join()