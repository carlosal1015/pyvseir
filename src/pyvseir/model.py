#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def SIRGeneral(
    t: float, s: float, i: float, beta: function, gamma: function
) -> np.array:
    """Right-hand side of the classic epidemic model SIR

    Args:
        t (float): Time.
        s (float): Susceptible faction.
        i (float): Infectious faction.
        beta (function): Contact rate.
        gamma (function): Inverse average infectious period.

    Returns:
        np.array: Evaluation of rhs [f_s(t,i,s), f_i(t,i,s)].
    """
    return np.array([-beta(t) * i * s, beta(t) * i * s - gamma(t) * i])
