my_nums=[3, -4, 2, -1, 6, -5]
success_tuples_list=[]
#assuming we have whole positive and negative number the sum we are looking for is 1
current_sum=10
def closest_to_zero(my_list):
    for index_1 in range(0,len(my_list)-1):
        for index_2 in range(index_1+1,len(my_list)):
            my_sum=my_list[index_1]+my_list[index_2]
            if  abs(my_sum)< current_sum:
                success_tuples_list.append((my_list[index_1],my_list[index_2]))
    return success_tuples_list
out=closest_to_zero(my_nums)
print(out)