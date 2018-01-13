from typing import List, Type  # noqa: F401

# Shortcuts for the import of the exporters

from .exporter import Exporter  # noqa: F401
from .ascii_exporter import ASCIIExporter  # noqa: F401
from .pixel_exporter import PixelExporter  # noqa: F401
from .png_exporter import PNGExporter  # noqa: F401
from .unicode_exporter import UnicodeExporter  # noqa: F401
from .wolf3d_exporter import Wolf3DExporter  # noqa: F401

EXPORTERS = [Wolf3DExporter, PNGExporter, PixelExporter,
             UnicodeExporter, ASCIIExporter]  # type: List[Type[Exporter]]
EXPORTER_NAMES = [x.__name__ for x in EXPORTERS]  # type: List[str]
