""" 
    Разработать программу, моделирующую один из алгоритмов управления памятью в 
    соответствии с вариантом задания. При моделировании считать что: 
        - объем моделируемой «памяти» составляет 64К; 
        - поступаемые на выполнение задачи содержатся в файлах, которые пользователь 
        может «загружать» в моделируемую «память» и выгружать из нее (файл 
        моделирует лишь размер задачи); 
        - размер задачи в диапазоне от 0 до 65535 байт. 
    Программа должна иметь возможность просмотра состояния моделируемой 
    «памяти». 
    Страничное распределение памяти 
""" 
size_page = int(input('Выберите размер страницы: ')) 
    
columns = 65535 // size_page 
memory = {} 
for i in range(columns + 1): 
    memory[i] = "0" * size_page
    
def task_in_memory(size_page, columns, memory):
    while True:
        deistvie = input("1 - Подать задачи\n2 - Назад\n")
        if deistvie == "1":
            kol_vo_tasks = int(input("Сколько задач хотите подать? "))
            for i in range(kol_vo_tasks):
                name_task = input("Введите название файла ")
                task = open(name_task, 'r') 
                symbols = len(task.read()) 
                task.close() 

                rez1 = symbols // size_page
                if rez1 == 0:
                    for n in range(columns + 1):
                        stroka = memory[n]
                        kol_vo_none = stroka.count("0")
                        if kol_vo_none >= symbols:
                            stroka = stroka.replace("0", "1", symbols)
                            memory[n] = stroka
                            print("Номер занятой страницы: ", n)
                            break
                else:
                    for i in range(rez1 + 1): 
                        if i != rez1: 
                            for n in range(columns + 1):
                                stroka = memory[n]
                                kol_vo_none = stroka.count("0")
                                if kol_vo_none == len(stroka):
                                    memory[n] = "1" * size_page
                                    print("Номер занятой страницы: ", n)
                                    break
                        else:
                            rez2 = symbols % size_page
                            for n in range(columns + 1):
                                stroka = memory[n]
                                kol_vo_none = stroka.count("0")
                                if kol_vo_none >= rez2:
                                    stroka = stroka.replace("0", "1", rez2)
                                    memory[n] = stroka
                                    print("Номер занятой страницы: ", n)
                                    break
        elif deistvie == "2":
            return
        else:
            print("Такого действия нет")
 
def inf_memory(memory):
    while True:
        deistvie = input("1 - Вывод всего пространста\n2 - Вывод 1 или несколько страницы\n3 - Назад\n")
        if deistvie == "1": 
            print(memory)
        elif deistvie == "2": 
            kol_vo_pages = int(input("Введите количество страниц: "))
            for i in range(kol_vo_pages): 
                number_pages = int(input("Введите номер страницы "))
                print(memory[number_pages])
        elif deistvie == "3":
            return
        else:
            print("Такого действия нет")
 
def delete_memory(columns, size_page, memory):
    while True:
        delete = input("1 - Очистить все пространство в памяти\n2 - Очистить одну или несколько страниц\n3 - Назад\n") 
        if delete == "1": 
            memory = {} 
            for i in range(columns + 1): 
                memory[i] = "0" * size_page 
        elif delete == "2": 
            kol_vo_delete = int(input("Введите количество страниц: "))
            for i in range(kol_vo_delete): 
                number_page1 = int(input("Введите номер страницы "))
                memory[int(number_page1)] = "0" * size_page 
        elif delete == "3":
            return
        else:
            print("Такого действия нет")

def main():
    menu = input("1 - Загрузка задачи в память\n2 - Вывод пространства\n3 - Удаление фрагмнетов памяти\nExit\n")
    while menu != "Exit":
        if menu == "1":
            task_in_memory(size_page, columns, memory)
        elif menu == "2":
            inf_memory(memory)
        elif menu == "3":
            delete_memory(columns, size_page, memory)
        else:
            print("Такой команды нет!")
        menu = input("1 - Загрузка задачи в память\n2 - Вывод пространства\n3 - Удаление фрагмнетов памяти\nExit\n")
    return
 

main()
