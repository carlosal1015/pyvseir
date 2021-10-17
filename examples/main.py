#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def time_points(a: int, b: int, n: int) -> np.arange:
    return a + (b - a) / (n + 1) * np.arange(n + 1)


def plot(run_model):
    from matplotlib import pyplot as plt

    # clear plots
    plt.close("all")

    # plot settings
    plt.rc("font", family="serif")
    plt.rcParams.update({"font.size": 12})
    # plotaspect = 2 / 3
    plt.plot(time_points, y[0, :], color="r", linewidth=2.0, label="s(t) Euler")
    plt.plot(time_points, y[1, :], color="b", linewidth=2.0, label="i(t) Euler")
    plt.plot(
        time_points, z[0, :], color="r", ls="--", linewidth=1.0, label="s(t) solver"
    )
    plt.plot(
        time_points, z[1, :], color="b", ls="--", linewidth=1.0, label="i(t) solver"
    )
    plt.title(f"Temporal development of the SIR model for R_0={R_0}")
    plt.xlabel("Time [days]")
    plt.ylabel("i(t)")
    plt.legend(loc="upper right")
    plt.grid(True)
    plt.show()


# @time_points(a=0, b=1e2, n=1e4)
def run_model(i0: float, s0: float, y0: np.array):

    i0 = 1e-2
    s0 = 1 - i0
    y0 = np.array([s0, i0])

    R_0 = 5
    gamma = 1 / 6.5
    beta = R_0 / 6.5

    """Set initial value, make it a 2D system of ODEs, set time interval.

    Args:
        i0 (float, optional): [description]. Defaults to 0.01.
        s0 ([type], optional): [description]. Defaults to 1-i0.
        y0 ([type], optional): [description]. Defaults to np.array([s0, i0]).
        a (int, optional): First day. Defaults to 0.
        b ([type], optional): Last day. Defaults to 1e2.
        n ([type], optional): Time steps. Defaults to 1e4.
    """


if __name__ == "__main__":
    from pyvseir.method import ForwardEuler
    from pyvseir.solver import ODEsolver
    from pyvseir.model import SIRGeneral

    # model = lambda t, y: SIRGeneral(t, y[0], y[1], beta, gamma)

    t_n = time_points(a=0, b=1e2, n=1e4)
    print(t_n)
    # y = ForwardEuler(model, y0, t_n)
    # z = ODEsolver(model, y0, t_n)
