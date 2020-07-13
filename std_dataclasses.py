"""
    Example of dataclasses module usage.
    This module let's to use class as a datatype to save data and access it
    through the dot-notation. Also it includes built-in methods like:
    * comparison (==)
    , also it has intuitive repr() output. And it also let's to decrease
    boiler-plate code.

    In case of implementing similar logic via regular classes, developer
    would need to implement methods by himself:
        * __str()__
        * __init()__
        * __repr()__
        * comparison method
        etc..

    dataclasses can also include methods, like distance_to shown below.

"""

from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2) ** 2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', lon=10.8, lat=59.9)  # pass values via keyword
vancouver = Position('Vancouver', -123.1, 49.3)  # pass values via positionals
print(f'Distance between {oslo.name} and {vancouver.name}: '
      f'{oslo.distance_to(vancouver)}')  # notice dot notation and method usage
