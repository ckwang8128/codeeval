import sys
from math import sqrt, ceil


def double_sqs(num):
    poss = [x**2 for x in range(0, int(ceil(sqrt(num)+1)))]
    seen_sums = []
    total_sums = 0
    for i in range(0,len(poss)): 
        if num - poss[i] in poss and num - poss[i] not in seen_sums:
            total_sums+=1
            seen_sums.append(poss[i])
    return total_sums


if __name__ == '__main__':
    number_of_vals = int(sys.stdin.readline().strip())
    for num in range(0, number_of_vals):
        print double_sqs(int(sys.stdin.readline().strip()))

