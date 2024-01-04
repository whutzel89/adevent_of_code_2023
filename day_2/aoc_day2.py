def test(file_in):
    file1 = open(file_in, 'r')
    Lines = file1.readlines()
    thresholds = {
        'red' : 13,
        'green' : 14,
        'blue' : 15
    }
    sum = 0

    for line in Lines:
        truth_list = []
        game_dict = {'red':[],'blue':[],'green':[]}
        game = int(line.split(':')[0].split(' ')[1])
        colors = line.replace(';',',').split(': ')[1].split(', ')
        temp = [game_dict[color.split(' ')[1].replace('\n','')].append(color.split(' ')[0]) for color in colors]
        truth_list = [all(int(i) < thresholds[key] for i in game_dict[key]) for key in game_dict.keys()]
        if all(truths == True for truths in truth_list):
            sum += game

    print(sum)
        #print(truth_list)
        #print(game_dict)
        #print(int(color.split(' ')[0]))
        # use generator to make list with true or flase for colors above (false) or below a given value (true)

if __name__ == "__main__":
    #test('/Users/whutzel/local_code/development/python/aoc_2023/day_2/example1.txt')
    test('/Users/whutzel/local_code/development/python/aoc_2023/day_2/star1.txt')
