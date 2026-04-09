import sys

from . import logger
from .constants import APP_TITLE
from ._version import __version__

if len(sys.argv) > 1:
    if sys.argv[1] == "-V" or sys.argv[1] == "--version":
        print(f'"{APP_TITLE}" version: {__version__}')
        sys.exit()

logger.info(
    f"{APP_TITLE} application started",
)
