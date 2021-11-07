#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np


def ForwardEuler(fun, y0: np.array, a: float, b: float, n: int) -> np.array:
    """[summary]

    Args:
        fun (function): Describes the right-hand side of the ODE.
        y0 (np.array): Initial value.
        a (float): Left boundary of the interval [a,b].
        b (float): Right boundary of the interval [a,b].
        n (int): Number of discretization points for the interval is n + 1.

    Returns:
        np.array: Contains the solution at the k-th time step as k-th column.
    """
    # set step size
    h: float = (b - a) / n

    # initialize solution
    y: np.zeros = np.zeros((np.size(y0), n + 1))

    # set initial value
    y[:, 0] = y0

    # iterations of the Euler Method
    for k in np.arange(n):
        y[:, k + 1] = y[:, k] + h * fun(a + k * h, y[:, k])

    return y
