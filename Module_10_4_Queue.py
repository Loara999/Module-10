import threading
import time
import random
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

    def __str__(self):
        return f'Table {self.number}'

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe():
    def __init__(self, *tables:Table):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests:Guest):
        for g in guests:
            empty_tables = (t for t in self.tables if not t.guest)
            try:
                t = next(empty_tables)
                t.guest = g
                g.start()

                print(f'{g.name} сел(-а) за стол номер {t.number}.')
            except StopIteration:
                self.queue.put(g)
                print(f'{g.name} в очереди.')

    def busy_tables(self):
        for t in self.tables:
            if t.guest:
                return (t for t in self.tables if t.guest)
            return 0

    def discuss_guests(self):
        while self.busy_tables() and not self.queue.empty():
            for t in self.tables:
                if t.guest:
                    if not t.guest.is_alive():
                        print(f'{t.guest.name} покушал(-а) и ушёл(-а).\n'
                              f'Стол номер {t.number} свободен.')
                        t.guest = None
                if not self.queue.empty() and not t.guest:
                    t.guest = self.queue.get()
                    print(f'{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}.')
                    t.guest.start()

        print('Кафе закрылось.')

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()


