def test(file_in):
    file1 = open(file_in, 'r')
    Lines = file1.readlines()
    sum = 0

    for line in Lines:
        game = line.split(':')[0].split(' ')[1]
        color = line.replace(';',',').split(': ')[1].split(', ')
