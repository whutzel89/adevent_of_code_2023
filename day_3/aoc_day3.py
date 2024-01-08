def test(in_file):
    file1 = open(in_file, 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        #print(line)
        s = [i for i,s in enumerate(line) if s.isdigit()] # this finds index of numbers
        # I think the next step will be to get consecutive integres from list, one method would be to iterate through list and check if next
        # value is +1 to current and append to list this should return a list of lists, [[0,1,2], [5,6,7],[12,13]]. Take these indexes then
        # check left and right of max min and below/above range
        print(s)
        #s = []
        #for t in line.split('.'):
        #    try:
        #        s.append(float(t))
        #    except ValueError:
        #        pass
        #print(s)
        
if __name__ == "__main__":
    test('/Users/whutzel/local_code/development/python/aoc_2023/day_3/example1.txt')
