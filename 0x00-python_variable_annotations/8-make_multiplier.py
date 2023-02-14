#!/usr/bin/env python3

"""Write a type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies
a float by multiplier."""

from typing import Callable, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    def x(n: float) -> float:
        return float(n * multiplier)

    return x
