from Class_logic import Logic

if __name__ == "__main__":
    print(f'{"*" * 3} Вас приветствует домашняя работа Марченко Олега {"*" * 3}')
    log = Logic()
    log.help()
    command = input('Что будем делать?: ')
    if command == '1':
        log.find_publisher_by_id()
    elif command == '2':
        log.find_publisher_by_name()
    elif command == '0':
        log.create_tables()
    elif command == '9':
        log.delete_tables()
    elif command == '8':
        log.fill_bd()
    else:
        print('Нераспознанная команда')