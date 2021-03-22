import collections

import time

import module

while True:
    print("\nВвеедите диапазон чисел->")
    p = int(input("Введите число ОТ:"))
    a =int(input("Введите число ДО:"))
    text1 = str([*range(p, a + 1)])  #итеррация вводимых значений
    text = text1.replace('[', '')
    text = text.replace(']', '')
    text = text.replace(',', '')
    text = text.replace(' ', '')

    module.col_symbol(text)
   


