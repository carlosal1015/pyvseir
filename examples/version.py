#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib as mpl
import numpy as np
import scipy as sc

NUMPY_VERSION = np.__version__
MATPLOTLIB_VERSION = mpl.__version__
SCIPY_VERSION = sc.__version__

message = f"""La versión de NumPy es {NUMPY_VERSION}.
La versión de Matplotlib es {MATPLOTLIB_VERSION}.
La versión de SciPy es {SCIPY_VERSION}."""

if __name__ == "__main__":
    print(message)
