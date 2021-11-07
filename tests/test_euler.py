#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

import pyvseir


def test_forwardEuler():
    pyvseir.ForwardEuler(fun=np.exp, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)
    pyvseir.ForwardEuler(fun=np.sin, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)
    pyvseir.ForwardEuler(fun=np.cos, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)
    # pyvseir.ForwardEuler(fun=np.log, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)
    pyvseir.ForwardEuler(fun=np.sinh, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)
    pyvseir.ForwardEuler(fun=np.cosh, y0=np.array([0.0, 0.0]), a=0, b=1, n=1000)


if __name__ == "__main__":
    test_forwardEuler()
