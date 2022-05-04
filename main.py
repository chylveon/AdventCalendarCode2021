# day 1
# open file and create list with all input

#read file:
input_list = []
with open('input01.txt', 'r') as input_0:
    for string_ in input_0:
        input_list.append(int(string_))

#testing list print(input_list[:7])

#compare elements in input_list to increment increasing
num_increasing = 0
current_num = 0
previous_num = 0
for num in input_list:
    current_num = num
    if previous_num != 0:
        if previous_num < current_num:
            num_increasing += 1
            previous_num = current_num
    previous_num = current_num

# print(num_increasing) returns 1564 which is correct.