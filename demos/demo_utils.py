# Temporarilly add parent folder to path (if not already added)
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from argparse import ArgumentTypeError
from typing import TYPE_CHECKING, List, Type, cast  # noqa: F401

if TYPE_CHECKING:
    from algorithms import Algorithm
    from exporters import Exporter
else:
    Algorithm = 'Algorithm'
    Exporter = 'Exporter'

from algorithms import ALGORITHMS, ALGORITHM_NAMES  # noqa: F401
from exporters import EXPORTERS, EXPORTER_NAMES  # noqa: F401

def validate_algorithm(desired_algorithm: str) -> Algorithm:
    ''' Check whether the algorithm name is valid and return an instance of it '''
    for algorithm in ALGORITHMS:
        if algorithm.__name__ == desired_algorithm:
            return algorithm()
    raise ValueError('Invalid algorithm. Valid algorithms: {}'.format('|'.join(
        [algorithm.__name__ for algorithm in ALGORITHMS])))

def avalible_algorithm(algorithm: str, available_algorithms: List[str]) -> Algorithm:
    ''' Check whether the algorithm name is in the list of avalible ones, and validate it '''
    if algorithm in available_algorithms:
        return validate_algorithm(algorithm)
    else:
        raise ValueError('Invalid algorithm. Avalible algorithms: {}'.format(
                         '|'.join(available_algorithms)))

def validate_exporter(desired_exporter: str) -> Exporter:
    ''' Check whether the exporter name is valid and return an instance of it '''
    for exporter in EXPORTERS:
        if exporter.__name__ == desired_exporter:
            return exporter()
    raise ValueError('Invalid exporter. Valid exporters: {}'.format('|'.join(
        [exporter.__name__ for exporter in EXPORTERS])))

def avalible_exporter(exporter: str, available_exporters: List[str]) -> Exporter:
    if exporter in available_exporters:
        return validate_exporter(exporter)
    else:
        raise ValueError('Invalid exporter. Avalible exporters: {}'.format(
                         '|'.join(available_exporters)))

def str2bool(v: str) -> bool:
    ''' https://stackoverflow.com/a/43357954/2531987 '''
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError('Boolean value expected')
