def test(in_file):
    file1 = open(in_file, 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        #print(line)
        #s = [int(s) for s in str.split(line,'.') if s.isdigit()]
        #print(s)
        s = []
        for t in line.split('.'):
            try:
                s.append(float(t))
            except ValueError:
                pass
        print(s)
        
if __name__ == "__main__":
    test('/Users/whutzel/local_code/development/python/aoc_2023/day_3/example1.txt')
