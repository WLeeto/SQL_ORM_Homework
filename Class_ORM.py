import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import *
from pprint import pprint
import json


class ORM:
    def __init__(self, password, database_name='nethologyHW', driver='postgresql://', user='postgres:', host='localhost:', host_port='5432/'):

        self.DSN = driver + user + password + host + host_port + database_name
        self.engine = sqlalchemy.create_engine(self.DSN)
        print(self.DSN)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        create_tables(self.engine)

    def delete_tables(self):
        delete_tables(self.engine)

    def _end_session(self):
        self.session.close()

    def _session_add(self, id, record):
        self.session.add(id, record)

    def find_publisher(self, id=None, name=None):
        if id is not None:
            for publisher in self.session.query(Publisher).filter(Publisher.id == id).all():
                print(publisher)
        elif name is not None:
            for publisher in self.session.query(Publisher).filter(Publisher.name == name).all():
                print(publisher)
        else:
            print('Ничего не найдено')
        self._end_session()

    def find_shop(self, publisher_id=None, publisher_name=None):
        if publisher_id is not None:
            for shop in self.session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == publisher_id).all():
                print(shop)
        elif publisher_name is not None:
            for shop in self.session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.name == publisher_name).all():
                print(shop)

    def fill_db(self, filepath):
        with open(filepath, 'r') as fd:
            data = json.load(fd)

        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            self.session.add(model(**record.get('fields')))
        self.session.commit()
        print('БД заполнена')


if __name__ == "__main__":
    db = ORM(password='6950dc6c7@')

    db.find_shop('Microsoft Press')