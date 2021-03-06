import numpy
from kaggle_environments import make

# create the environment. You can also specify configurations for seed and loglevel as shown below. If not specified, a random seed is chosen. 
# loglevel default is 0. 
# 1 is for errors, 2 is for match warnings such as units colliding, invalid commands (recommended)
# 3 for info level, and 4 for everything (not recommended)
# set annotations True so annotation commands are drawn on visualizer
# set debug to True so print statements get shown
env = make("lux_ai_2021", configuration={"seed": 562124210, "loglevel": 2, "annotations": True}, debug=True)

# run a match between two simple agents, which are the agents we will walk you through on how to build!
steps = env.run(["simple_agent", "simple_agent"])
# if you are viewing this outside of the interactive jupyter notebook / kaggle notebooks mode, this may look cutoff
# render the game, feel free to change width and height to your liking. We recommend keeping them as large as possible for better quality.
# you may also want to close the output of this render cell or else the notebook might get laggy
out = env.render(mode="html", width=1200, height=800)

# write the output html file
with open('../../runs/output.html', 'w') as f:
    f.write(out)