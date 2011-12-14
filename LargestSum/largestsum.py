import sys

def largest_cont_sum(num_array):
    max_at_element = max_so_far = float("-inf")
    for num in num_array:
        max_at_element = max(max_at_element + num, num)
        max_so_far = max( max_at_element, max_so_far)
    return max_so_far

with open(sys.argv[1], 'r') as input_file:
    for line in input_file:
        print largest_cont_sum(map(int, line.strip().split(',')))
    input_file.close()
