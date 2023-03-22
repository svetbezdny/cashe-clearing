import os
import shutil
import time
from tqdm import tqdm

path = r'C:\Users\user\Desktop\Кэш.txt'    # файл с директориями для очистки

start = time.time()

print('Очистка началась')
print()

lst = []
with open(path) as files:
    for file in files:
        lst.append(file.strip())

try:
    for i in tqdm(lst):
        for j in os.listdir(i):
            if j.find('.') != -1:
                try:
                    os.remove(f'{i}\\{j}')
                except:
                    continue
            else:
                try:
                    shutil.rmtree(f'{i}\\{j}')
                except:
                    continue

    finish = round(time.time() - start) // 60, round(time.time() - start) % 60
    print('Кэш очищен.', f'Время выполнения - {finish[0]} мин., {finish[1]} сек.', sep = '\n')
except Exception as e:
    print('Что-то пошло не так:', e, sep = '\n')