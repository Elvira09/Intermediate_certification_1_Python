import csv
import model.the_note as n
import util.config as c
import service.service as s


path = c.path
field = [
    '№ ',
    'Заголовок заметки ',
    'Текст заметки ',
    'Дата записи '
]


def write_data(path):
    with open(path, 'a') as file:
        csv_writer = csv.writer(file, delimiter=";")
        csv_writer.writerow(n.note())
    file.close()


def write_edit_data(path):
    with open(path, 'w+') as file:
        csv_writer = csv.DictWriter(file, delimiter=";", fieldnames=field)
        csv_writer.writeheader()
        csv_writer.writerows(s.edit_note())
    file.close()


def write_del_data(path):
    with open(path, 'w+') as file:
        csv_writer = csv.DictWriter(file, delimiter=";", fieldnames=field)
        csv_writer.writeheader()
        csv_writer.writerows(s.del_note())
    file.close()


# def input_field(path):
#     with open(path, 'w+') as file:
#         csv_writer = csv.DictWriter(file, delimiter=";", fieldnames=field)
#         csv_writer.writeheader()
#     file.close()

