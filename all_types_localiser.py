from psychopy import core, visual, event
import os
from glob import glob
import random

# Set escape key
escape_key = 'escape'


# Get current folder
cwd = os.getcwd()

# Get all the folders in the stimuli folder
folders = glob(os.path.join(cwd, 'stimuli', '*'))

# Add every movie file in those folders to our stimuli dict, using the folders as keys
all_files = {}

for folder in folders:
    files = glob(os.path.join(folder, '*.mov'))

    all_files[folder] = files

# Create our window
win = visual.Window([1024, 768], units="pix",
                    fullscr=True, allowGUI=False,
                    color=(0, 0, 0))

win.mouseVisible = False

# Create a cross stimulus
fix = visual.TextStim(win, text='+')


# Create our stimuli
all_stimuli = []

# We want two sets, each containing one block of each type of stimuli
for i in range(2):
    # Create a list for everything in this set
    set = []

    for stimulus_type in all_files:  # Run through each stimulus type
        # Extract them from the files dict
        stimuli_files = all_files[stimulus_type]

        chosen_files = random.choices(stimuli_files, k=6)  # Choose 6 of them

        # Now generate movie stimuli from the 6 files we chose
        block = []

        for file in chosen_files:
            stim = visual.MovieStim3(
                win, filename=file, noAudio=True, units='norm', size=(2, 2))

            block.append(stim)  # Add the stimuli to the block

        set.append(block)  # And the block to the set
        # random.shuffle(set)

    all_stimuli.append(set)  # And the set to the all stimuli list


# Add the wait until 5 is pressed?

timing = win.flip()

# Run the experiment
for set in all_stimuli:
    # Show a rest block
    fix.draw()
    win.flip()
    core.wait(18)

    for block in set:
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


# Add a final rest block
fix.draw()
win.flip()
core.wait(18)

timing2 = win.flip()
print(f'The length of time the experiment took is {timing2 - timing}')

win.close()
core.quit()
