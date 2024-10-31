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

    @staticmethod
    def get_celestial_body_count() -> int:
        return CelestialBody.count 

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def mass(self) -> float:
        return self._mass

    @mass.setter
    def mass(self, mass: float):
        self._mass = mass

    def get_info(self):
        return f"Имя: {self.name}, Масса: {self.mass} солнечная масса"


class Star(CelestialBody):
    def __init__(self, name: str, mass: float, temperature: int):
        super().__init__(name, mass) 
        self._temperature = temperature  

    def describe(self):
        return f"{self.name} - звезда с температурой {self._temperature} K."

    def generate_flare(self):
        flare_strength = random.randint(1, 10)
        if flare_strength <= 3:
            return f"На {self.name} произошла слабая солнечная вспышка с силой {flare_strength}!"
        elif flare_strength <= 7:
            return f"На {self.name} произошла средняя солнечная вспышка с силой {flare_strength}!"
        else:
            return f"На {self.name} произошла сильная солнечная вспышка с силой {flare_strength}!"


class Planet(CelestialBody):
    def __init__(self, name: str, mass: float, distance_from_star: float):
        super().__init__(name, mass) 
        self._distance_from_star = distance_from_star  

    def describe(self):
        return f"{self.name} - планета, расположенная на расстоянии {self._distance_from_star} а.е. от своей звезды."

    def calculate_orbit_time(self):
        orbit_period_years = (self._distance_from_star ** 1.5)  
        return f"{self.name} требуется примерно {orbit_period_years:.2f} лет для совершения одного оборота."


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

star.name = "Новое Солнце"
star.mass = 1.1
print(star.get_info())  