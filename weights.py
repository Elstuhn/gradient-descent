import numpy as np
import typing as t
from typing import Callable

tensor = t.Union(np.ndarray, list)

def weightdescent(costeqn : str, weights : tensor):
    