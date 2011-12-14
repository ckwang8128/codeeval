import sys
import re

with open(sys.argv[1], 'r') as tests:
    for line in tests:
        line = line.strip()
        #If we just have a blank line, don't do anything with it.
        if line == '\n':
            continue
        if re.match('^([A-Z]|[a-z]|[0-9])+@([A-Z]|[a-z]|[0-9])*.(eu|com|gov|edu|org)', line):
            print 'true'
        else:
            print 'false'
        
