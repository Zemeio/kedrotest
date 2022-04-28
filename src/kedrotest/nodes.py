"""
This is a boilerplate pipeline
generated using Kedro 0.18.0
"""

import logging
from typing import Any, Callable, Dict, Tuple
from PIL.Image import Image
import numpy as np
import pandas as pd


def split_data(
    data: Dict[str, Callable[[], Image]]
) -> Image:

    return data
