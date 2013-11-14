import os
import subprocess


def width(mechanism='tput'):
    if mechanism == 'stty':
        stty_size = os.popen('stty size', 'r').read()
        rows, columns = map(int, stty_size.split())
    else:
        tput_cols = subprocess.check_output(['tput', 'cols'])
        columns = int(tput_cols)
    return columns
