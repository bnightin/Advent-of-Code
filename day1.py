column_one_list = []
column_two_list = []
sum = 0

with open('input.txt') as infile:
    for line in infile:
        #get the numbers in both columns of input.txt and put them into lists
        column_one = line.split()[0]
        column_one_list.append(int(column_one))
        column_two = line.split()[1]
        column_two_list.append(int(column_two))
    #sort the lists from smallest to largest
    sorted_column_one = sorted(column_one_list)
    sorted_column_two = sorted(column_two_list)
    #find differences
    for i, k in zip(sorted_column_one, sorted_column_two):
            difference = abs(i - k)
            sum += difference 
    print(sum)
