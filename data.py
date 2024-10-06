class Data:
    valid_login = 'Alex2020'
    valid_password = 'abc123'
    valid_firstname = 'Alex'
    valid_courier_data = {'login': 'Alex2020', 'password': 'abc123', 'firstName': 'Alex'}
    courier_data_without_name = {'login': 'Alex2020', 'password': '9876'}
    courier_data_with_wrong_password = {'login': 'Alex2020', 'password': 'abcdef'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Андрей',
        'lastName': 'Миронов',
        'address': 'Ленинский проспект, 25',
        'metroStation': 5,
        'phone': '+79001234567',
        'rentTime': 3,
        'deliveryDate': '2024-06-26',
        'comment': 'Как я хочу кататься',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Екатерина',
        'lastName': 'Смирнова',
        'address': 'Проспект Победы, 14',
        'metroStation': 12,
        'phone': '+79876543210',
        'rentTime': 7,
        'deliveryDate': '2024-06-28',
        'comment': 'Зима близко, нужно кататься.',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Софья',
        'lastName': 'Звягина',
        'address': 'Речная улица, 8',
        'metroStation': 20,
        'phone': '+70991122334',
        'rentTime': 1,
        'deliveryDate': '2024-06-30',
        'comment': 'Давно хотел попробовать кататься на самокате',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Дарья',
        'lastName': 'Соколова',
        'address': 'Красный переулок, 5',
        'metroStation': 3,
        'phone': '+77771112233',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Позвонить мне за десять минут',
        'color': []
    }
