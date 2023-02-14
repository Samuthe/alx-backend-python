#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: int, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
