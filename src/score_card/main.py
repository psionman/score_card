import sys

from score_card import logger
from score_card.constants import APP_TITLE
from score_card._version import __version__
from score_card.score_gui import ScoreCardApp

if len(sys.argv) > 1:
    if sys.argv[1] == "-V" or sys.argv[1] == "--version":
        print(f'"{APP_TITLE}" version: {__version__}')
        sys.exit()

logger.info(
    f"{APP_TITLE} application started",
)

ScoreCardApp().run()
