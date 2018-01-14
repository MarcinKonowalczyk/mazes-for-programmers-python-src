from typing import Type

import pytest

import pathfinders.dijkstra as Dijkstra
import pathfinders.longest_path as LongestPath

from algorithms import ALGORITHMS, Algorithm
from base import DistanceGrid, Grid

# All combinations of odd / even + uneven sizes
TEST_SIZES = ((9, 9), (10, 10),
              (5, 10), (10, 5), (5, 9), (9, 5),
              (6, 10), (10, 6), (6, 9), (9, 6))

# TODO: Add start / end to the grid
# TODO: Add something to the algorithm to mark whether it generates a fully connected grid
# TODO: Test whether the grids generated are fully connected

@pytest.mark.parametrize('algorithm', ALGORITHMS)
def test_algorithms_all_run(algorithm: Type[Algorithm]) -> None:
    for size in TEST_SIZES:
        grid = Grid(*size)

        try:
            algorithm().on(grid)
        except Exception as ex:
            raise ex

@pytest.mark.parametrize('algorithm', ALGORITHMS)
def test_basic_pathfinding(algorithm: Type[Algorithm]) -> None:
    for size in TEST_SIZES:
        grid = DistanceGrid(*size)
        algorithm().on(grid)

        try:
            start, end = LongestPath.calculate(grid)
            Dijkstra.calculate_distances(grid, start, end)
        except Exception as ex:
            raise ex
