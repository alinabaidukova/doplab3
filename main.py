from functools import reduce

def right(last, now):
    if now[0] > last[0]:    #если первый эл-т новости > первого эл-та предыдущей:
        print(' '.join(now[1])) #вывод этой строки
        return now  #возвращение этой строки
    else:
        return last #возвращение предыдущей строки

news = open('news.txt', 'r', encoding="utf8")
array = []  #список для эл-тов файла
for line in news.readlines():   #readlines читает каждую строку и возвращает список
    count, *text = line.split() #разбитие строки на эл-ты: 1й эл-т как число, остальные как текст (текст идёт в список)
    array.append([int(count), text])    #создание списка из числа и списка с текстом

print(' '.join(array[0][1]))   #вывод в строку текст 1й строки
reduce(right, array)    #сравнивание чисел и возвращение максимального


