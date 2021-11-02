# for kaggle-environments
from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES, Position
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate
import math
import sys

from utils import *
from agent import *
import numpy as np

from kaggle_environments import make



# define the environment and run our agent through it
env = make("lux_ai_2021", configuration={"seed": 562124210, "loglevel": 2, "annotations": True}, debug=True)

steps = env.run([agent, "simple_agent"])

out = env.render(mode="html", width=1200, height=800)

# write the output html file
with open('../../runs/output.html', 'w') as f:
    f.write(out)