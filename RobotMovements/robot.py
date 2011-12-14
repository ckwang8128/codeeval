from sets import Set



def generate_successors(square, length, width):
    """Returns a list of the successors from *square*
   on a board of length *length* and width *width*

   Arguments: 
   
   square - a tuple of x,y coordinates on a grid
   length - positive integer corresponding to len of grid
   width - positive integer corresponding to width of grid
   """
    successor_list = []
    cur_x = square[0]
    cur_y = square[1]
    for i in [-1,1]:
        if 0<=cur_y+i<=length-1:
            successor_list.append((cur_x, cur_y+i))
        if 0<=cur_x+i<=width-1:
            successor_list.append((cur_x+i, cur_y))
    return successor_list

if __name__ == '__main__':
    LENGTH = 4
    WIDTH = 4
    visited = Set()
    fringe = []
    start = (0,0)
    visited.add(start)
    num_ways = 0
    for i in generate_successors(start, LENGTH, WIDTH):
        fringe.append(i)
    while fringe:
        poss_visit = fringe.pop()
        if poss_visit == (3,3):
            num_ways += 1
            continue
        if poss_visit not in visited:
            visited.add(poss_visit)
            for i in generate_successors(poss_visit, LENGTH, WIDTH):
                fringe.append(i)
    print num_ways
