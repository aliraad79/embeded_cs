class Parking:
    def __init__(self) -> None:
        self.capacitty = 10
        self.current_plates = []

    def add_car(self, plate):
        if plate in self.current_plates:
            print("Car is Already in parking")
        elif len(self.current_plates) == self.capacitty:
            print("Parking Full")

        else:
            self.current_plates.append(plate)

    def car_exits(self, plate):
        if plate not in self.current_plates:
            print("Car is Not in parking")
        else:
            self.current_plates.remove(self.current_plates.index(plate))
