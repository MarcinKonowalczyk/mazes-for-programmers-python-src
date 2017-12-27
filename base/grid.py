from random import randrange
from typing import cast, Generator, List, Optional, Tuple

from base.cell import Cell


class Grid:

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def size(self) -> int:
        return self.rows * self.cols

    @property
    def shape(self) -> Tuple[int, int]:
        return self.rows, self.cols

    @property
    def deadends(self) -> List[Cell]:
        return [cell for cell in self.each_cell() if len(cell.links) == 1]

    def __init__(self, rows: int, cols: int) -> None:
        if rows is None or rows < 2:
            raise ValueError('Rows must be an integer greater than 1')
        if cols is None or cols < 2:
            raise ValueError('cols must an integer greater than 1')

        self._rows = rows     # type: int
        self._cols = cols     # type: int
        self._grid = self.prepare_grid()
        self.configure_cells()

    # def cell_at(self, row: int, column: int) -> Optional[Cell]:
    #     if not (0 <= row < self.rows):
    #         return None
    #     if not (0 <= column < self.cols):
    #         return None
    #     return self._grid[row][column]

    # def set_cell_at(self, row: int, column: int, cell: Cell) -> None:
    #     self._grid[row][column] = cell

    def prepare_grid(self) -> List[List[Cell]]:
        ''' Create the grid'''
        return [[Cell(row, column) for column in range(self.cols)] for row in range(self.rows)]

    def configure_cells(self) -> None:
        ''' Create all the north/sout/east/west dependencies of the cells '''
        for cell in self.each_cell():
            row = cell.row
            col = cell.col

            cell.north = self[row-1,col]
            cell.south = self[row+1,col]
            cell.east  = self[row,col+1]
            cell.west  = self[row,col-1]

    def __getitem__(self,key):
        ''' Get grid item method '''
        if type(key) == int:
            # One key therefore return row
            if key < 0 or key > self.rows-1: return None
            return self._grid[key]
        elif type(key) == tuple and len(key) == 2:
            # Two keys therefore return element
            row, col = key
            if row < 0 or row > self.rows-1: return None
            if col < 0 or col > self.cols-1: return None
            return self._grid[row][col]
        else:
            raise IndexError
    
    def __setitem__(self, key, item):
        ''' Set grid item method '''
        if type(key) == int:
            if 0 <= key <= self.rows-1:
                self._grid[key] = item
        elif type(key) == tuple and len(key) == 2:
            row, col = key
            if 0 <= row <= self.rows-1 and 0 <= col <= self.cols-1:
                self._grid[row][col] = item
        else:
            raise IndexError

    def random_cell(self) -> Cell:
        ''' Return random cell '''
        row = randrange(0,self.rows)
        col = randrange(0,self.cols)
        return self[row,col]

    def each_row(self) -> Generator:
        ''' Access each row '''
        for row in self._grid:
            yield row

    def each_col(self) -> Generator:
        ''' Access each column '''
        for col in zip(*self._grid):
            yield col

    def each_cell(self) -> Generator:
        ''' Access each cell '''
        for row in self.each_row():
            for cell in row:
                yield cell

    def contents_of(self, cell: Cell) -> str:
        return '   '
