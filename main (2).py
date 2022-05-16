import numbers
import sqlite3

import self as self

data = sqlite3.connect('cars.DB')

cursor = data.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
                NAME CHAR(15) NOT NULL,
                MODEL CHAR (25) NOT NULL)''')

data.commit()


class Accaunt:
    def init(self, name, model):
        self.name = name
        self.model = model

    def add_car(self):
        self.name = input('Enter name: ')
        self.model = input('Enter model: ')
        add_car_into_db = '''INSERT INTO cars(NAME < MODEL) VALUES (?, ?)'''
        cursor.execute(add_car_into_db, (self.name, self.model))
        data.commit()

    def del_car(self):
        self.name = input('Enter name: ')
        self.model = input('Enter model: ')
        del_car_into_db = '''DELETE FROM cars WHERE NAME =? AND MODEL = ?'''
        cursor.execute(del_car_into_db, (self.name, self.model))
        data.commit()

    def update_car(self):
        self.name = input('Enter name: ')
        self.model = input('Enter model: ')
        self.update_name = input('Enter new name: ')
        self.update_model = input('Enter new model: ')
        update_car_from_db = '''UPDATE cars SET NAME = ?, MODEL = ? WHERE NAME = ? AND MODEL = ?'''
        cursor.execute(update_car_from_db, (self.update_name, self.update_model, self.name, self.model))
        data.commit()

    def details(self):
        cursor.execute('''SELECT * FROM cars''')
        print(cursor.fetchall())

    def start(self):
        self.number = input(
            "Select letter of operation (\n R - Show All InformationFrom DB \n I - Add Car into db \n D - Delete car from db \n U - Update car from db): ")

        accaunt = Accaunt()
        if self.number == 'R' or self.number == 'r':
            accaunt.details()
            accaunt.start()

        elif self.number == 'I' or self.number == 'i':
            accaunt.add_car()
            accaunt.details()
            accaunt.start()

        elif self.number == 'D' or self.number == 'd':
            accaunt.del_car()
            accaunt.details()
            accaunt.start()

        elif self.number == 'U' or self.number == 'u':
            accaunt.update_car()
            accaunt.details()
            accaunt.start()

accaunt = Accaunt()
accaunt.start()


