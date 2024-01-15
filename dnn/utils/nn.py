from dataclasses import dataclass
import math
from typing import Tuple, List


@dataclass
class Coord:
    x: float
    y: float
    pass


@dataclass
class DistComparison:
    c1: int
    c2: int
    d: float
    pass


def least(dcs: list[DistComparison]) -> list[DistComparison]:
    holder = []
    for d in dcs:
        holder.append(d.d)
        pass
    m = min(holder)
    return [d for d in dcs if d == m]
    pass


def distance(a: Coord, b: Coord) -> float:
    return math.fabs(a.x - b.x) + math.fabs(a.y - b.y)
    pass


def get_nn(coords: list[Coord]) -> list[DistComparison]:
    dcs = []
    for i, c in enumerate(coords):
        for j, cc in enumerate(coords):
            if j == i:
                continue
                pass
            dcs.append(DistComparison(i, j, distance(c, cc)))
            pass
        pass
    return least(dcs)
    pass


def get_nn_str(s: str) -> tuple[bool, None, str] | tuple[bool, list[DistComparison], None]:
    coords = s.split(';')
    dcs = []
    for c in coords:
        cs = c.split(',')
        if len(cs) == 2:
            try:
                dcs.append(Coord(float(cs[0]), float(cs[1])))
                pass
            except ValueError:
                return False, None, "Invalid coordinate"
                pass
            pass
        else:
            return False, None, "Malformed coordinate"
            pass
        pass
    if len(dcs) == 0:
        return False, None, "No coordinates"
        pass

    return True, get_nn(dcs), None
    pass
