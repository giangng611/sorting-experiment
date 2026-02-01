from __future__ import annotations
from typing import List, Optional
import random
from base_sorter import BaseSorter


class QuickSortRandomPivot(BaseSorter):
    """
    Quick Sort using a random pivot.

    Helps avoid worst-case behavior of fixed pivot selection.
    """