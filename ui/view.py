def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False
    

def menu():
    print('Добавить заметку: 			выберете 1\n'
    	'Найти заметку: 				выберете 2 \n'
        'Изменить заметку: 			выберете 3\n'
        'Удалить заметку: 			выберете 4\n'
		'Посмотреть все заметки:  		выберете 5\n')
    
def get_action():
    menu()
    choice = input('Выберите вариант: ')
    while (not is_int(choice)) or (int(choice) < 1 or int(choice) > 5): 
        choice = input('Некорректный ввод, сделайте выбор повторно:  ')
    choice = int(choice)
    return choice

    