from datetime import datetime

from django.shortcuts import render


def index(request, tvno=0):
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tv_list = [
        {'name': '李榮浩《不遺憾》', 'tvcode': 'VR0Cl19hTTU'},
        {'name': '徐子未《慢冷》', 'tvcode': 'KD6MG3YXPDo'},
        {'name': '魏宏宇《Tom&Jerry》', 'tvcode': 'Bl6kIYBBnJA'},
    ]
    tvno = tvno
    tv = tv_list[tvno]

    return render(request, 'index.html', locals())


def engtv(request, tvno=0):
    now = datetime.now()
    tv_list = [
        {'name': 'Shape of You', 'tvcode': 'JGwWNGJdvx8'},
        {'name': 'Faded', 'tvcode': '60ItHLz5WEA'},
        {'name': 'Chandelier', 'tvcode': '2vjPBrBU-TM'},
    ]
    tvno = tvno
    tv = tv_list[tvno]

    return render(request, 'engtv.html', locals())


def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda']
    car_list = [
        [],
        ['Fiesta', 'Focus', 'Modeo', 'EcoSport'],
        ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
        ['Mazda3', 'Mazda5', 'Mazda6'],
    ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]

    return render(request, 'carlist.html', locals())


def carprice(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [{'model': 'Fiesta', 'price': 203500}, {'model': 'Focus', 'price': 605000}],
        [{'model': 'Fit', 'price': 564524}, {'model': 'Odyssey', 'price': 12457}],
        [{'model': 'Mazda3', 'price': 3434543}, {'model': 'Mazda5', 'price': 7243214}],
    ]
    maker = maker
    maker_name = car_maker[maker]
    cars = car_list[maker]

    return render(request, 'carprice.html', locals())
