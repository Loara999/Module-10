import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 100
        while counter:
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            elif self.lock.locked() or len(threading.enumerate()) == 2:
                r = random.randint(50, 500)
                self.balance += r
                print(f'Пополнение: {r}. Баланс: {self.balance}')
                counter -= 1
                time.sleep(0.001)

    def take(self):
        counter = 100
        while counter:
            if not self.lock.locked():
                r = random.randint(50, 500)
                print(f'Запрос на снятие {r}')
                if r <= self.balance:
                    self.balance -= r
                    print(f'Снятие: {r}. Баланс: {self.balance}')
                    counter -= 1
                else:
                    print('Запрос отклонён, недостаточно средств.')
                    self.lock.acquire()



bk = Bank()
t_deposit = threading.Thread(target=Bank.deposit, args=(bk,))
t_take = threading.Thread(target=Bank.take, args=(bk,))
t_deposit.start()
t_take.start()
t_deposit.join()
t_take.join()
print(f'Итоговый баланс: {bk.balance}.')
