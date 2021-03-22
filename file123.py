import time

import math


def prostoe_chislo():


    """Finding a prime number"""
    p = int(input("\nВведите число(>2):"))
    if p > 1:
        for z in range(2, p):
            if (p % z == 0):
                print("Число составное\n")
                time.sleep(2)
                break         
            else:
                print("Число простое\n")
                time.sleep(2)
        else:
            print("Число должно быть > 1 Ведите заново\n")
            time.sleep(2)


def search_nod():
    """Find a NOD"""
    a = int(input("\nВведите число a:"))
    a = abs(a)
    b = int(input("Введите число b:"))
    b = abs(b)

    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else: 
            b = b % a
    print("НОД =", a + b) 
    time.sleep(2)

def search_nok():
    """Find a NOK"""
    a = int(input("\nВведите число a:"))
    a = abs(a)
    b = int(input("Введите число b:"))
    b = abs(b)
    z = abs(a * b)

    while (a != 0 and b != 0):
        if a > b:
            a = a % b
        else: 
            b = b % a
    nod = a + b
    nok = z / nod
    print("NOK =", nok) 
    time.sleep(2)


while True:
    step = input("""
Какие вычисления будем проводить?
Простое число          -  1
Вычеслить НОД          -  2
Вычеслить НОК          -  3
Выход                  -  Enter
Что выбираем:""")

    if not step:
        print("Печалька...")
        time.sleep(1)
        break
    elif step == "1":
        prostoe_chislo()
    elif step == "2":
        search_nod()
    elif step == "3":
        search_nok()
    else:
        print("Повторите")
        time.sleep(3)

        
    