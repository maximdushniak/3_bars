import json
import math


def load_data(filepath):
    data = []
    with open(filepath) as datafile:
        data = json.loads(datafile.read())
    return data


def get_biggest_bar(data):
    max_seats_count = 0
    biggest_bar = []
    for i in data:
        if i['Cells']['SeatsCount']>=max_seats_count:
            max_seats_count =  i['Cells']['SeatsCount']
            biggest_bar = i

    return biggest_bar


def get_smallest_bar(data):
    min_seats_count = 0
    smallest_bar = []
    for i in data:
        if i['Cells']['SeatsCount']<=min_seats_count:
            min_seats_count =  i['Cells']['SeatsCount']
            smallest_bar = i

    return smallest_bar


def get_closest_bar(data, longitude, latitude):

    min_l = 0
    closest_bar = []
    for i in data:
        i_longitude = float(i['Cells']['geoData']['coordinates'][0]) #
        i_latitude = float(i['Cells']['geoData']['coordinates'][1])

        l = math.sqrt(math.pow((i_longitude - longitude), 2) + math.pow((i_latitude - latitude), 2))

        if l<=min_l:
            min_l = l
            closest_bar = i

    return closest_bar


if __name__ == '__main__':

    # filepath = 'Бары.json'
    filepath = input(u'Имя файла [Бары.json]: ')
    if not filepath:
        filepath = 'Бары.json'
    data = load_data(filepath)

    # самый большой
    biggest_bar = get_biggest_bar(data)
    print(biggest_bar)

    # Самый большой
    smallest_bar = get_smallest_bar(data)
    print(smallest_bar)

    # Ближайший
    longitude, latitude = input('Долгота [37.621587946152012]: '), input('Широта: [55.765366956608361]')
    # 'Name': 'Юнион Джек'
    # 37.621587946152012, 55.765366956608361
    if not longitude:
        longitude = 37.621587946152012
    if not latitude:
        latitude = 55.765366956608361
    closest_bar = get_closest_bar(data, longitude, latitude)
    print(closest_bar)
