from typing import List, Type  # noqa: F401

# Shortcuts for the import of the algorithms

from .algorithm import Algorithm  # noqa: F401
from .aldous_broder import AldousBroder  # noqa: F401
from .binary_tree import BinaryTree  # noqa: F401
from .hunt_and_kill import HuntAndKill  # noqa: F401
from .recursive_backtracker import RecursiveBacktracker  # noqa: F401
from .sidewinder import Sidewinder  # noqa: F401
from .wilson import Wilson  # noqa: F401

ALGORITHMS = [AldousBroder, BinaryTree, HuntAndKill,
              RecursiveBacktracker, Sidewinder, Wilson]  # type: List[Type[Algorithm]]
ALGORITHM_NAMES = [x.__name__ for x in ALGORITHMS]  # type: List[str]
