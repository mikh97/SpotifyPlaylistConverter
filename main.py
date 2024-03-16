import os
import subprocess
import sys  # for sys.executable (The file path of the currently using python)
from spotdl import __main__ as spotdl # To get the location of spotdl

file = open('url.txt', 'r')

# User Input
count = 0
out = "GC"
cmd = "spotdl --bitrate 320k --format mp3 "
output = "--output \'~/" + out + "\'"

for line in file:
    url = line.splitlines()

    try:
        dl = " --download \'" + url[0] + "\'"
        full_cmd = cmd + output + dl
        print(full_cmd)
        # Download for os.system
        print(subprocess.run(full_cmd, shell=True))
    except:
        print("Can't download: " + url)
        count + 1

file.close()

print(count)
