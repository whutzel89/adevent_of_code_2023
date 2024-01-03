def test(file_in):
    file1 = open(file_in, 'r')
    Lines = file1.readlines()
    sum = 0

    for line in Lines:
        game_dict = {'red':[],'blue':[],'green':[]}
        game = int(line.split(':')[0].split(' ')[1])
        colors = line.replace(';',',').split(': ')[1].split(', ')
        temp = [game_dict[color.split(' ')[1].replace('\n','')].append(color.split(' ')[0]) for color in colors]
        print(game_dict)
        #print(int(color.split(' ')[0]))
        # use generator to make list with true or flase for colors above (false) or below a given value (true)

if __name__ == "__main__":
    test('/Users/whutzel/local_code/development/python/aoc_2023/day_2/example1.txt')
