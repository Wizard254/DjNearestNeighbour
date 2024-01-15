from dataclasses import dataclass
import math
from typing import Tuple, List


@dataclass
class Coord:
    """
    Model the x-y coordinate system
    """
    x: float
    y: float
    pass


@dataclass
class DistComparison:
    """
    Records the distance between any two coordinates, c1 and c2, as d
    """
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
    return [d for d in dcs if d.d == m]
    pass


def distance(a: Coord, b: Coord) -> float:
    """
    :param a: first coordinate
    :param b: second coordinate
    :return: the Manhattan Distance between the two coordinates, a and b
    """
    return math.fabs(a.x - b.x) + math.fabs(a.y - b.y)
    pass


def get_nn(coords: list[Coord]) -> list[DistComparison]:
    """
    :param coords: list of coordinates in the x-y grid-system
    :return: pairs of coordinates that are, the points that are closest to each other
    """
    dcs = []
    distances = []

    # For each coordinate, get the manhattan distance to each of the other coordinates
    for i, c in enumerate(coords):
        for j, cc in enumerate(coords):
            if j <= i:
                # Avoid duplicate coodinate comparison (Permutations)
                continue
                pass
            d = distance(c, cc)
            distances.append(d)
            dcs.append(DistComparison(i, j, d))
            pass
        pass
    # Get the least manhattan distance comparison
    m = min(distances)
    # Return all instances that may have tied for the least manhattan distance
    return [d for d in dcs if d.d == m]
    # return least(dcs)
    pass


def get_nn_str(s: str) -> tuple[bool, None, str] | tuple[bool, str, None]:
    """
    Accepts a string representation of coordinates in a 2D plane, parses coordinates
    then gets the pairs of coordinates that are the closest to each other
    :param s: string representation of coordinates in a 2D plane
    :return: tuple of a boolean that determines whether the operation was successful,
    a string representation of coordinates that are the closest to each other,
    and an appropriate error massage
    """
    # Records all defined coordinates
    coords = []
    # Map each coordinate defined in the string to the Coord class
    for c in s.split(';'):
        cs = c.split(',')
        if len(cs) == 2:
            try:
                coords.append(Coord(float(cs[0]), float(cs[1])))
                pass
            except ValueError:
                # We had issues converting coordinate string to float
                return False, None, "Invalid coordinate"
                pass
            pass
        else:
            # expected two coordinates, more or less were provided
            return False, None, "Malformed coordinate"
            pass
        pass

    if len(coords) == 0:
        # No coordinates were parsed
        return False, None, "No coordinates"
        pass

    # Get objects of manhattan distance comparisons between coordinates
    nn = get_nn(coords)
    # Make a string representation of the coordinates
    out = ''
    for i, c in enumerate(nn):
        c1 = coords[c.c1]
        c2 = coords[c.c2]

        if i != 0:
            # FIXME: Can we have more than two pairs of points, as close to each other?
            out += '-'
            pass
        # FIXME: Are we restricted to integers?
        # out += f'{c1.x},{c1.y};{c2.x},{c2.y}'
        out += f'{int(c1.x)},{int(c1.y)};{int(c2.x)},{int(c2.y)}'
        pass

    return True, out, None
    pass
