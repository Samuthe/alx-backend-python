#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float."""

from typing import Union


def sum_mixed_list(mxd_lst: Union[int, str]) -> float:
    return sum(float(mxd_lst))
