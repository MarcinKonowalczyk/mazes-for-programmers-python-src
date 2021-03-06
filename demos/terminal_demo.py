# Temporarilly add parent folder to path (if not already added)
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import argparse
from typing import Union, cast  # noqa: F401

from base import DistanceGrid
# from base.grid import Grid
from base import Rotator

import pathfinders.dijkstra as Dijkstra
import pathfinders.longest_path as LongestPath

from demos.demo_utils import ALGORITHM_NAMES, str2bool, avalible_algorithm, avalible_exporter

DEFAULT_EXPORTER = 'UnicodeExporter'
AVAILABLE_EXPORTERS = ['ASCIIExporter', 'UnicodeExporter']
AVAILABLE_ALGORITHMS = ALGORITHM_NAMES

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Render a maze')
    parser.add_argument('rows', type=int, help='number or rows')
    parser.add_argument('cols', type=int, help='number or columns')
    parser.add_argument('algorithm', type=str, help='algorithm to use')
    parser.add_argument('-e', '--exporter', type=str, default=DEFAULT_EXPORTER,
                        help='maze exporter to use')
    parser.add_argument('-r', '--rotations', type=int, default=0,
                        help='integer value measuring number of 90 degree clockwise rotations to perform')
    parser.add_argument('-p', '--pathfinding', type=str2bool, default=False,
                        help='whether to find the path through the maze')
    args = parser.parse_args()

    algorithm = avalible_algorithm(args.algorithm, AVAILABLE_ALGORITHMS)
    exporter = avalible_exporter(args.exporter, AVAILABLE_EXPORTERS)
    rotations = args.rotations
    pathfinding = args.pathfinding
    rows = args.rows
    cols = args.cols
    print('Algorithm: {}\nRows: {}\ncolumns: {}\nExporter: {}'.format(args.algorithm, rows, cols, args.exporter))
    print('90deg Rotations: {}\nPathfinding: {}'.format(rotations, pathfinding))

    grid = DistanceGrid(rows, cols)

    algorithm.on(grid)

    for num in range(rotations):
        grid = cast(DistanceGrid, Rotator().on(grid))

    if pathfinding:
        start, end = LongestPath.calculate(grid)
        print('Solving maze from row {} column {} to row {} column {}'.format(*start, *end))
        Dijkstra.calculate_distances(grid, start, end)

    exporter.render(grid)

    print('Maze has {} dead-ends'.format(len(grid.deadends)))
