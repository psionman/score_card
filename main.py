# main.py (at project root)
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", "score_card"))

from main import ScoreCardApp
ScoreCardApp().run()
