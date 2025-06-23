my_nums=[3, -4, 2, -1, 6, -5]

def closest_to_zero(my_list):
    for index_1 in range(len(my_list)):
        for index_2 in range(my_list[index_1:]):
            print(f"Index 1 is {index_1} and index 2 is {index_2}")
closest_to_zero(my_nums)