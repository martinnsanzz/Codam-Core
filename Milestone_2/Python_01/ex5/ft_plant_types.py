#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int,
                 growth_rate: float) -> None:
        self.name = name
        self._height = (height, 15.0)[height < 0]
        self._plant_age = (plant_age, 10)[plant_age < 0]
        self.growth_rate = growth_rate
        self.week_growth = 0.0
        if (height < 0):
            print("Height can't be negative")
        if (plant_age < 0):
            print("Age can't be negative")

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, ", end="")
        print(f"{self._plant_age} days old")

    def age(self) -> None:
        self._plant_age += 1
        self._height += self.growth_rate
        self.week_growth += self.growth_rate

    def grow(self, days: int) -> None:
        self.show()
        for x in range(1, days + 1):
            self.age()
            print(f"=== Day {x} ===")
            self.show()
            if (x % 7 == 0):
                print(f"Growth this week: {round(self.week_growth, 1)}cm")
                self.week_growth = 0

    def set_height(self, amount: float):
        if amount > 0:
            self._height = amount
            print(f"Height updated: {round(amount)}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, amount: int):
        if amount > 0:
            self._plant_age = amount
            print(f"Age updated: {amount} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._plant_age)
    

class Flower(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 growth_rate: float, color: str) -> None:
        super().__init__(name, height, plant_age, growth_rate)
        self.color = color

    def bloom():
        ...

class Tree(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 growth_rate: float, trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age, growth_rate)
        self.trunk_diameter = trunk_diameter

    def produce_shade():
        ...

class Vegetable(Plant):
    def __init__(self, name: str, height: float, plant_age: int,
                 growth_rate: float, harvest_season: bool,
                 nutritional_value: chr) -> None:
        super().__init__(name, height, plant_age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

if __name__ == "__main__":
    vegi: Vegetable = Vegetable("Carrot", 0.5, 5, 0.2, False, 'A')

    vegi.show()