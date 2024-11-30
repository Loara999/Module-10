import threading
import time
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            r = random.randint(50, 500)
            self.balance += r
            print(f'Пополнение: {r}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            r = random.randint(50, 500)
            print(f'Запрос на снятие {r}')
            if r <= self.balance:
                self.balance -= r
                print(f'Снятие: {r}. Баланс: {self.balance}')
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
