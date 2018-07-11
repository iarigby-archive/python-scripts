import os
import sys

ext = ".PNG"
try:
    for i in range(int(sys.argv[1]), int(sys.argv[2]), -1):
        os.rename(str(i)+ext, str(i+1)+ext)
except:
    print("could not resolve arguments")
    exit()
