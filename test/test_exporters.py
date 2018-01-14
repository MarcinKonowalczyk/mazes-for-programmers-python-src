from typing import Type

import pytest

from algorithms import BinaryTree
from base import Grid
from exporters import EXPORTERS, Exporter

# Square, tall, wide
TEST_SIZES = ((10, 10), (10, 5), (5, 10))

@pytest.mark.parametrize('exporter', EXPORTERS)
def test_exporters_all_run(exporter: Type[Exporter]) -> None:

    if exporter.__name__ == 'Wolf3DExporter': return  # Skip the Wolf3D exporter for a time being

    for size in TEST_SIZES:
        grid = Grid(*size)
        BinaryTree().on(grid)

        try:
            # filename = '{}x{}_test_exporters_all_run[{}]'.format(*size, exporter.__name__)
            filename = 'temp'
            exporter().render(grid, filename=filename)
        except Exception as ex:
            raise ex
