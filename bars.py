import json
import math
import os
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', nargs='?')

    return parser


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def input_coord(coord_name=''):
    try:
        return float(input('Введите координату ' + coord_name + ' :'))
    except ValueError:
        return None


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['Cells']['SeatsCount'])

    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['Cells']['SeatsCount'])

    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda x:
        math.sqrt((x['Cells']['geoData']['coordinates'][0] - longitude)**2
                  + (x['Cells']['geoData']['coordinates'][1] - latitude)**2))

    return closest_bar


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    
    if namespace.filepath:
        filepath = namespace.filepath
    else:
        filepath = input(u'Имя файла [data.json]: ')
        if not filepath:
            filepath = 'data.json'
    data = load_data(filepath)

    if data is not None:
        biggest_bar = get_biggest_bar(data)
        print("Самый большой бар:", biggest_bar)

        smallest_bar = get_smallest_bar(data)
        print("Самый маленький бар:", smallest_bar)

        longitude = input_coord('Долгота')
        latitude = input_coord('Широта:')

        if latitude is None or longitude is None:
            print('Введены неверные координаты')
        else:
            closest_bar = get_closest_bar(data, longitude, latitude)
            print('Ближайший бар:', closest_bar)
    else:
        print('Файл не найден.')
