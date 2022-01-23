from turtle import st
from psychopy import core, visual, event
import os
from glob import glob
import random

escape_key = 'escape'

cwd = os.getcwd()

# Specify the folders we want
face_folder = os.path.join(cwd, 'stimuli', 'Faces')
scene_folder = os.path.join(cwd, 'stimuli', 'Scenes')

win = visual.Window([1024, 768], units="pix",
                    fullscr=False, allowGUI=True,
                    color=(0, 0, 0))

#win.mouseVisible = False

# Load in stimuli files
face_files = glob(os.path.join(face_folder, '*.mov'))
scene_files = glob(os.path.join(scene_folder, '*.mov'))
all_files = [face_files, scene_files]
'''
all_stimuli = []
for i in range(5):
    for file_type in all_files:
        chosen_files = random.choices(file_type, k=6)
        block = []
        for file in chosen_files:
            stim = visual.MovieStim3(
                win, filename=file, noAudio=True, units='norm', size=(2, 2))
            block.append(stim)
        
        all_stimuli.append(block)
'''
# Create face and scene stimuli
face_stimuli = []
scene_stimuli = []

for file in face_files:
    # Units and norm set the videos to be fullscreen
    stim = visual.MovieStim3(
        win, filename=file, noAudio=True, units='norm', size=(2, 2))
    face_stimuli.append(stim)

for file in scene_files:
    stim = visual.MovieStim3(
        win, filename=file, noAudio=True, units='norm', size=(2, 2))
    scene_stimuli.append(stim)

all_stimuli = []

# Generate 5 blocks of each type of stimuli with 6 vids each, randomly chosen
for i in range(5):
    f_block = random.choices(face_stimuli, k=6)
    s_block = random.choices(scene_stimuli, k=6)

    # Save the blocks to our overall list of stimuli
    all_stimuli.append(f_block)
    all_stimuli.append(s_block)

# random.shuffle(all_stimuli)

# Run each block at a time
for block in all_stimuli:
    for mov in block:
        # Draw each stimuli
        while mov.status != visual.FINISHED:
            mov.draw()
            win.flip()

        # If the escape key is pressed, end the experiment
        keys = event.getKeys(keyList=[escape_key])

        if len(keys) > 0:
            print('User requested to quit, ending experiment')
            win.close()
            core.quit()

win.close()
core.quit()
