#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from scipy.integrate import ode


def ODEsolver(fun: function, y0: list, a: float, b: float, n: int):
    # set step size
    h: float = (b - a) / n

    # initialize solution
    y: np.zeros = np.zeros((np.size(y0), n + 1))

    # set initial value
    y[:, 0] = y0

    r: ode = ode(fun).set_integrator("vode", method="bdf")
    r.set_initial_value(y0, a)
    # r.set_f_params(2.0).set_jac_params(2.0)
    for k in np.arange(n):
        y[:, k] = r.integrate(r.t + h)

    return y
