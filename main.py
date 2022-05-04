# day 1
# open file and create list with all input

#read file:
input_list = []
with open('input01.txt', 'r') as input_0:
    for string_ in input_0:
        input_list.append(int(string_))

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
list_len = len(input_list)
i = 0
j = 1
k = 2
sum_list = []
while k < (list_len):
    while j < (list_len - 1):
        while i < (list_len - 2):
            sum_of_AAA = input_list[i] + input_list[j] + input_list[k]
            sum_list.append(sum_of_AAA)
            i += 1
            j += 1
            k += 1

print(sum_list[:7])

# repeat comparison from before with sum_list instead of input_list:
num_increasing = 0
current_num = 0
previous_num = 0
for num in sum_list:
    current_num = num
    if previous_num != 0 and previous_num != current_num:
        if previous_num < current_num:
            num_increasing += 1
    previous_num = current_num

print(num_increasing)