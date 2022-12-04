# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    transport_amount = 3

    def transport_info(self, transport_amount= 3):
        """
        Show transport info
        """
        res = f'I have {transport_amount} different modes of transportation.'
        return res


class Car(Transport):

    transport_type = 'car'
    model = 'Volvo'
    mileage = 23456

    def car_info(self):
        """
        Show car info
        """
        res = f'I have {self.transport_amount} different modes of transportation. My {self.transport_type} is {self.model}, its mileage is {self.mileage} mi'
        return res

class Plane(Transport):
    transport_type = 'plane'
    model = 'Mriya'
    mileage = 58654

    def plane_info(self):
        """
        Show plane info
        """
        res = f'I have {self.transport_amount} different modes of transportation. My {self.transport_type} is {self.model}, its mileage is {self.mileage} mi'
        return res

class Ship(Transport):
    transport_type = 'ship'
    model = 'Neptun'
    mileage = 125000

    def ship_info(self):
        """
        Show ship info
        """
        res = f'I have {self.transport_amount} different modes of transportation. My {self.transport_type} is {self.model}, its mileage is {self.mileage} mi'
        return res


transport = Transport()
print(transport.transport_info())

car1 = Car()
print(car1.car_info())

plane1 = Plane()
print(plane1.plane_info())

ship1 = Ship()
print(ship1.ship_info())