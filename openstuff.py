import os
import subprocess

#command is what you give it
stream = os.popen(command, 'r', 1)
stream.read()