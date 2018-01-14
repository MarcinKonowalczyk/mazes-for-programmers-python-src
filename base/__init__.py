# TODO: Unify Grid and DistanceGrid...?
from typing import List, Type  # noqa: F401

# Shortcuts for the import of the base classes
from .cell import Cell  # noqa: F401
from .grid import Grid  # noqa: F401
from .colored_grid import ColoredGrid  # noqa: F401
from .distances import Distances  # noqa: F401
from .distance_grid import DistanceGrid  # noqa: F401
from .rotator import Rotator  # noqa: F401

GRIDS = [Grid, ColoredGrid, DistanceGrid]  # type: List[Type[Grid]]
GRID_NAMES = [x.__name__ for x in GRIDS]  # type: List[str]
