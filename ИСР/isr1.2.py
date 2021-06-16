"""
    Дополнить программу для считывания данных проверкой утверждений или высказываний (assert). Создать отдель-
    ный блок для такой проверки (с помощью __name__) и скрипт командной строки для запуска этих проверок.
    Шеховцова Е. Г.
"""

import json

def main():
    di = dictionary()
    keys = list(di[0].keys())
    str0, str1 = table(di, keys)
    print(str0)
    print(str1)


def dictionary():
    """
        Формирование словаря из файла
    """
    try:
        with open('MOCK_DATA.json') as jFile:
            lines = json.load(jFile)
        jFile.close()
    except FileNotFoundError:
        print('Файл не найден')
    return lines


def table(di, keys):
   
    str0 = ""
    str1 = ""
    s = 0
    for l in di:
        for i in keys:
            if s== 0:
                str0 += "|{:27}|".format(i)
            str1 += "|{:27}|".format(l[i])
        str1 += "\n\r"
        s += 1
    return str0, str1

if __name__ == '__table__':
    assert(type(di) != list), 'Неверный формат json'

main()
