class Car():

    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels


class Bike(Car):  # Car 클래스를 상속받는다.

    def __init__(self, fuel, wheels, size):
        super().__init__(fuel, wheels)  # 부모 클래스의 생성자를 호출한다.
        self.size = size


if __name__ == "__main__":
    bike = Bike("gas", 2, "small")
    print(bike.fuel, bike.wheels, bike.size)
