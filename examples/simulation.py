#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# ------------------------------------------------------
# Initialization for SIR and generalized SIR
# ------------------------------------------------------

# set time interval
a: int = 0
b: int = 100  # maximum days
n: int = 10000  # #time steps

time_points: np.arange = a + (b - a) / (n + 1) * np.arange(n + 1)

# set initial value
i0: float = 0.01
s0: float = 1 - i0
y0: np.array = np.array([s0, i0])  # make it a 2D system of ODEs


# ---------------------------------------------------------------------
# Example for SIR with R_0=1.5 (beta=5/6.5, gamma=1/6.5) R_0=s0*beta/gamma
# ---------------------------------------------------------------------

# set parameters
R_0: float = 5.0
gamma: float = 1 / 6.5
beta: float = R_0 / 6.5


"""
# nonconstant beta
def beta(t):
    if np.sin(np.pi / 7 * t) >= 0:
        return 0.8
    else:
        return 0
"""

# initialize rhs
SIR = lambda t, y: SIRGeneral(t, y[0], y[1], beta, gamma)

# solve ODE
y = ForwardEuler(SIR, y0, a, b, n)

z = ODEsolver(SIR, y0, a, b, n)

# plot infectious and susceptible faction
# plt.figure()
plt.plot(time_points, y[0, :], color="r", linewidth=2.0, label="s(t) Euler")
plt.plot(time_points, y[1, :], color="b", linewidth=2.0, label="i(t) Euler")
plt.plot(time_points, z[0, :], color="r", ls="--", linewidth=1.0, label="s(t) solver")
plt.plot(time_points, z[1, :], color="b", ls="--", linewidth=1.0, label="i(t) solver")
plt.title(f"Temporal development of the SIR model for R_0={R_0}")
plt.xlabel("Time [days]")
plt.ylabel("i(t)")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()
