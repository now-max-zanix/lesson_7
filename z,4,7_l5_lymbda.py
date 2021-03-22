from functools import reduce

import time

def fact_rec():
    """Search factoril with lamda(recursion)"""
    while True:
        y = input("\nВведите не отрицательное целое число:")
        try:
            int(y)
        except ValueError:
            print("\nСори....НУЖНО ВВЕСТИ ЧИСЛО")
            continue
        else:
            y = int(y)
            if y < 0:
                print("\nНаписано же НЕ ОТРИЦАТЕЛЬНОЕ")
                continue
            else:
                break

    fact = lambda x: 1 if x == 0 else x * fact(x-1)  #Calculating the factorial
    print("Факториал числа {} равен ={}".format(y, fact(y)))
    time.sleep(2)
  

def fact_norec():
    """Search factoril with lamda( non recursion)"""
    while True:
        y = input("\nВведите не отрицательное целое число:")
        try:
            int(y)
        except ValueError:
            print("\nСори....НУЖНО ВВЕСТИ ЧИСЛО")
            continue
        else:
            y = int(y)
            if y < 0:
                print("\nНаписано же НЕ ОТРИЦАТЕЛЬНОЕ")
                continue
            else:
                break

    fact = reduce(lambda y,z: y * z,range(1, y+1))  #Calculating the factorial (recirsia)
    print("Факториал числа {} равен ={}".format(y, fact))
    time.sleep(2)


while True:
    step = input("""
Как будем вычислять факториал?
Лямбда С (Рекурсией)           -  1
Лямбда БЕЗ (Рекурсии)          -  2
Выход                          -  Enter
Что выбираем:""")

    if not step:
        print("Печалька...")
        time.sleep(1)
        break
    elif step == "1":
        fact_rec()
    elif step == "2":
        fact_norec()
    else:
        print("Повторите")
        time.sleep(3)
 
