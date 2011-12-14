import sys

def longest_common_sub(x, y):
    '''
    Returns the longest common subsequence between strings x and y
    '''
    #we need both x and y to be non-empty
    if x and y:
        if x[-1] == y[-1]:
            return longest_common_sub(x[0:-1], y[0:-1]) + [x[-1]]
        else:
            return max(longest_common_sub(x[0:-1], y),
                       longest_common_sub(x, y[0:-1]), key=len)
    else:
        return []


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as test_file:
        for line in test_file:
            if line.strip() == '':
                continue
            print ''.join(longest_common_sub(line.strip().split(';')[0], line.strip().split(';')[1])).strip()
        test_file.close()
