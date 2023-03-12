import csv
import util.config as c


path = c.path

def reader_data(path):
    data = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)
    file.close()
    return data
