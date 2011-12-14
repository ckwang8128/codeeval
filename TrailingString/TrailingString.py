import sys

with open(sys.argv[1], 'r') as tests:
    for line in tests:
        line = line.strip('\n')
        if line == '':
            continue
        whole_str = line.split(',')[0]
        substr = line.split(',')[1]
        if whole_str[-len(substr):len(whole_str)] == substr: 
            print 1 
        else:
            print 0
    tests.close()
