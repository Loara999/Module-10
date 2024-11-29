import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w+', encoding='utf-8')as file:
        for w in range(word_count):
            file.write(f'Какое-то слово №{w}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def count_time():
    start_time = time.time()
    yield
    end_time = time.time()
    result_time = round(end_time - start_time, 2)
    print(f'Время выполнения программы: {result_time}.')

for _ in count_time():
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

args_ = [(10, 'example5.txt'),
         (30, 'example6.txt'),
         (100, 'example8.txt'),
         (200, 'example7.txt')]
func = (threading.Thread(target=write_words, args=a) for a in args_)
for _ in count_time():
    threading.current_thread().join()
    for thread in func:
        thread.start()