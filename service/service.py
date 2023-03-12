import util.data_reader as r
import model.the_note as n
import util.config as c
import ui.view as v


path = c.path
data = r.reader_data(path)

def show_notes():
    for item in data:
        print(item)


def del_note():
    data_new = []
    count = 0
    search = input('Введите данные для поиска:  ')
    for item in data:
        for value in item.values():
            if search in value:
                count +=1
                print(item)
    if count == 0:
        print('Поиск не дал результата: ')
        data_new = data
    else:
        choice = input('Подтвердите номер заметки : ')
        while (not v.is_int(choice)): 
            choice = input('Некорректный ввод, сделайте выбор повторно:  ')
        choice = int(choice)
        data.pop(choice - 1)
        
        numbering = 1
        for item in data:
            edit = \
                {
                '№ ': numbering,
                'Заголовок заметки ': item['Заголовок заметки '] ,
                'Текст заметки ': item['Текст заметки '],
                'Дата записи ': item['Дата записи ']
                }
            numbering +=1
            data_new.append(edit)

    return data_new
# print(del_note())


def edit_note():
    data_new = []
    count =0
    search = input('Введите данные для поиска редактируемой заметки: ')
    for item in data:
        for value in item.values():
            if search in value:
                count +=1
                print(item)

    if count == 0:
        print('Поиск не дал результата: ')
        data_new = data
    else:
        choice = input('Подтвердите номер редактируемой заметки: ')        
        while ((not v.is_int(choice))): 
            choice = input('Некорректный ввод, сделайте выбор повторно:  ')
        choice = int(choice)
        editable = data[choice - 1]
        data.pop(choice - 1)

        data_new = data
        edit = \
                    {
                    '№ ': editable.get('№ '),
                    'Заголовок заметки ': editable.get('Заголовок заметки '),
                    'Текст заметки ': n.get_note_body(),
                    'Дата записи ': n.get_date_time()
                    }
        data_new.append(edit)
        data_new.sort(key=lambda dictionary: dictionary['№ '])
    return data_new
# print(edit_note())

def search_note():
    count = 0
    search = input('Введите данные для поиска: ')
    for elem in data:
        for value in elem.values():
            if search in value:
                count +=1
                print(elem)
    if count == 0:
        print('Поиск не дал результата')

