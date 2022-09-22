from Class_ORM import ORM


class Logic:
    def __init__(self):
        print(f'{"*" * 3} Давайте создадим подключение к БД {"*" * 3}\n'
              f'{"*" * 3} Чтобы осавить значение по умолчанию просто оставьте поле пустым {"*" * 3}')

        driver = input('Введите название драйвера (по умолчанию "postgresql"): ')
        if not driver:
            driver = 'postgresql://'
        else:
            driver += '://'
        user = input('Введите имя пользователя (по умолчанию "postgres"): ')
        if not user:
            user = 'postgres:'
        else:
            user += ':'
        password = input('Введите пароль пользователя: ')
        password += '@'
        host = input('Где распологается БД (по умолчанию "localhost"): ')
        if not host:
            host = 'localhost:'
        else:
            host += ':'
        host_port = input('Введите номер порта (по умолчанию "5432"): ')
        if not host_port:
            host_port = '5432/'
        else:
            host_port += '/'
        database_name = input('Введите название БД: ')

        self.db = ORM(password=password, database_name=database_name, driver=driver, user=user, host=host, host_port=host_port)

    def delete_tables(self):
        self.db.delete_tables()

    def create_tables(self):
        self.db.create_tables()

    def find_publisher_by_id(self):
        id = input("Введите id издателя: ")
        self.db.find_publisher(id=id)

    def find_publisher_by_name(self):
        name = input("Введите имя: ")
        self.db.find_publisher(name=name)

    def fill_bd(self):
        file = input('Введите путь до фаила')
        self.db.fill_db(filepath=file)

    def help(self):
        print('Я умею делать следующее:\n'
              '1 - Поиск издателя по id\n'
              '2 - Поиск издателя по имени\n'
              '0 - Создать структуру БД согласно заданию\n'
              '9 - Удалить структуру БД\n'
              '8 - Заполнить БД (в разработке)\n')

