from datetime import datetime
import util.config as c
import util.data_reader as r


path = c.path

def get_unid():
    return (len(r.reader_data(path)) + 1)
    # with open(path, 'r', encoding='utf-8') as file:
    #     unid = len(file.readlines())
    # return unid

# print(get_unid())

def get_note_title():
    return input('Введите заголовок заметки: ')

def get_note_body():
    return input('Введите текст заметки: ')

def get_date_time():
    return datetime.now().strftime("%d/%m/%y %I:%M")


def note():
    data = \
        [
        get_unid(),
        get_note_title(),
        get_note_body(),
        get_date_time()
        ]
    return data

