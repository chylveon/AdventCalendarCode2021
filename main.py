# day 1
# open file and create list with all input


#testing list print(input_list[:7])

#compare elements in input_list to increment increasing
#num_increasing = 0
#current_num = 0
#previous_num = 0
#for num in input_list:
#    current_num = num
#    if previous_num != 0:
#        if previous_num < current_num:
 #           num_increasing += 1
 #           previous_num = current_num
 #   previous_num = current_num

# print(num_increasing) returns 1564 which is correct.

# second question day 1
#list_len = len(input_list)
#i = 0
#j = 1
#k = 2
#sum_list = []
#while k < (list_len):
#    while j < (list_len - 1):
#        while i < (list_len - 2):
#            sum_of_AAA = input_list[i] + input_list[j] + input_list[k]
#            sum_list.append(sum_of_AAA)
#            i += 1
#            j += 1
#            k += 1

#print(sum_list[:7])

# repeat comparison from before with sum_list instead of input_list:
#num_increasing = 0
#current_num = 0
#previous_num = 0
#for num in sum_list:
#    current_num = num
#    if previous_num != 0 and previous_num != current_num:
#        if previous_num < current_num:
#            num_increasing += 1
#    previous_num = current_num

# print(num_increasing)

# day 02
#read file:
current_input = None
input_list = []
# opens file then separates input into list of lists.
with open('input02.txt', 'r') as input_1:
    for line in input_1:
        line = line.strip().split(' ')
        input_list.append(line)

# print(input_list[:7])

# compare outputs based on first [][0]
i = 0
horizontal_position = 0
depth = 0
#print(input_list[:7])

for each_list in input_list[:]:
    for index, elem in enumerate(each_list[:]):
        if index == 1:
            each_list[index] = int(elem)

#print(input_list[:7])

i = 0
while i != len(input_list):
    # if direction == forward add to horizontal position
    if input_list[i][0] == 'forward':
        horizontal_position += input_list[i][1]
    # if direction == up subtract from depth
    if input_list[i][0] == 'up':
        depth -= input_list[i][1]
    # if direction == down add to depth
    if input_list[i][0] == 'down':
        depth += input_list[i][1]
    i += 1

depth_by_hor_pos = horizontal_position * depth
print(depth_by_hor_pos)