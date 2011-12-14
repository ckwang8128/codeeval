import sys

with open(sys.argv[1], 'r') as tests:
    for line in tests:
        
        #If we just have a blank line, don't do anything with it.
        if line == '\n':
            continue
        
        entry = line.strip().split(';')
        n = int(entry[0])
        num_list = map( int , entry[1].split(','))
        #formula for sum of range from 0-(n-2)
        desired_sum = ((n-2)**2 + (n-2)) / 2
        actual_sum = sum(num_list)
        print actual_sum - desired_sum
    tests.close()
