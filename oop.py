import random
from abc import ABC, abstractmethod

class CelestialBody(ABC):
    count = 0

    def __init__(self, name: str, mass: float):
        self._name = name 
        self._mass = mass  
        CelestialBody.count += 1  

    @abstractmethod
    def describe(self):
        pass  

    @classmethod
    def get_celestial_body_count(cls):
        return cls.count 

    def get_info(self):
        return f"Имя: {self._name}, Масса: {self._mass} солнечная масса"


class Star(CelestialBody):
    def __init__(self, name: str, mass: float, temperature: int):
        super().__init__(name, mass) 
        self._temperature = temperature  

    def describe(self):
        return f"{self._name} звезда с температурой {self._temperature} K."

    def generate_flare(self):
        flare_strength = random.randint(1, 10)
        return f"На {self._name} произошла солнечная вспышка с силой {flare_strength}!"


class Planet(CelestialBody):
    def __init__(self, name: str, mass: float, distance_from_star: float):
        super().__init__(name, mass) 
        self._distance_from_star = distance_from_star  

    def describe(self):
        return f"{self._name} планета, расположенная на растоянии {self._distance_from_star} а.е. от своей звезды."

    def calculate_orbit_time(self):
        orbit_period_years = (self._distance_from_star ** 1.5)  
        return f"{self._name} требуется примерно {orbit_period_years:.2f} лет для совершения одного оборота."

if __name__ == "__main__":
    star = Star(name="Солнце", mass=1.0, temperature=5772)
    planet_earth = Planet(name="Земля", mass=1.0, distance_from_star=1.0)
    planet_mars = Planet(name="Марс", mass=0.107, distance_from_star=1.52)

    print(star.describe())  
    print(planet_earth.describe()) 
    print(planet_mars.describe())  

    print(star.generate_flare())
    print(planet_earth.calculate_orbit_time())  
    print(planet_mars.calculate_orbit_time())  

    print(f"Создано небесных тел: {CelestialBody.get_celestial_body_count()}") 
