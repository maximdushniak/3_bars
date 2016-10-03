import json
import math
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    index_biggest_bar = max(range(len(data)), key=lambda x: data[x]['Cells']['SeatsCount'])
    biggest_bar = data[index_biggest_bar]

    return biggest_bar


def get_smallest_bar(data):
    index_smallest_bar = min(range(len(data)), key=lambda x: data[x]['Cells']['SeatsCount'])
    smallest_bar = data[index_smallest_bar]

    return smallest_bar


def get_closest_bar(data, longitude, latitude):

    index_closets_bar = min(range(len(data)), key=lambda x: math.sqrt((data[x]['Cells']['geoData']['coordinates'][0] - longitude)**2 + (data[x]['Cells']['geoData']['coordinates'][1] - latitude)**2))
    closest_bar = data[index_closets_bar]

    return closest_bar


if __name__ == '__main__':

    filepath = input(u'Имя файла [data.json]: ')
    if not filepath:
        filepath = 'data.json'
    data = load_data(filepath)

    if data is None:
        pass
    else:
        # самый большой
        biggest_bar = get_biggest_bar(data)
        print("Самый большой бар:", biggest_bar)

        # Самый маленький
        smallest_bar = get_smallest_bar(data)
        print("Самый маленький бар:", smallest_bar)

        # Ближайший
        try:
            longitude  = float(input('Долгота [37.621587946152012]: '))
        except ValueError:
            longitude = None

        try:
            latitude = float(input('Широта: [55.765366956608361]: '))
        except ValueError:
            latitude = None

        if not (latitude is None or longitude is None):
            closest_bar = get_closest_bar(data, longitude, latitude)
            print('Ближайший бар:', closest_bar)
        else:
            print('Введены неверные координаты')