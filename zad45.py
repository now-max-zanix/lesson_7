import time

def mnojestvo():
    """Removing duolicate items"""
    string1 = input("\nВведите первый список:")
    list1 = list(string1)
    print(list1)
    
    set1 = set(list1)
    print(set1)
    time.sleep(2)

def check():
    open_list = ["[","{","(","<"]
    close_list = ["]","}",")",">"]

    text = input("\nВведите данные:")


    def proverka(text):
        """Cheking for the corrrectness of parenthese"""
        stack = []
        for i in text:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                ind = close_list.index(i) #Assigning an index
                if stack and (open_list[ind] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    return "Не корректно раставлены скобки"
        if len(stack) == 0:
            return "Ошибок нет"
        else:
            return "Не хватает скобок(ки)"
    print(proverka(text))
    time.sleep(2)

while True:
    print(
"""
Выберите задачу.
Удалить из списка повторяющиеся элементы:    1
Правильно ли расставлены скобки:             2
Выход:                                       Enter
"""
    )
    next_step = input("\nВведите: ")
    if not next_step:
        print("Удачи...")
        break
    elif next_step == "1":
        mnojestvo()
    elif next_step == "2":
        check()
    else:
        print("Повторите ввод")