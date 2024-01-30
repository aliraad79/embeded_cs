class FullParking(Exception):
    ...


class DuplicatedCar(Exception):
    ...


class UnknownCar(Exception):
    ...


class Car:
    def __init__(self, plate: str, enter_time: int) -> None:
        self.plate = plate
        self.enter_time = enter_time

    def __eq__(self, __value: object) -> bool:
        return self.plate == __value.plate


class Parking:
    def __init__(self) -> None:
        self.current_cars: list[Car] = []

    def get_capacity(self):
        return 10 - len(self.current_cars)

    def add_car(self, plate, time):
        temp_car = Car(plate, None)
        if temp_car in self.current_cars:
            raise DuplicatedCar()
        elif len(self.current_cars) == self.get_capacity():
            raise FullParking()
        else:
            self.current_cars.append(Car(plate, time))

    def car_exits(self, plate):
        temp_car = Car(plate, None)
        if temp_car not in self.current_cars:
            raise UnknownCar
        else:
            return self.current_cars.pop(self.current_cars.index(temp_car))

    def welcome(self, plate: str):
        print("Welcome", plate)

    def goodbye(self, plate: str):
        print("GoodBye", plate)
