
def recursive_binary_search(target, source, left=0):

    if len(source) == 0:
        return -1
    center = (len(source)-1) // 2
    if source[center] == target:

        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def rotated_array_search(input_list, number):

    def recursive_rotate_search(mid_index, end_value, travel = len(input_list) // 2):

        if input_list[mid_index] > input_list[mid_index + 1]:
            return mid_index

        if input_list[mid_index] < input_list[mid_index - 1]:
            return mid_index - 1

        move_by = travel // 2

        if input_list[mid_index] > end_value:

            next_index = mid_index + move_by

            return recursive_rotate_search(next_index, end_value, move_by)

        if input_list[mid_index] < end_value:

            next_index = mid_index - move_by

            return recursive_rotate_search(next_index, end_value, move_by)

    end_value = input_list[len(input_list) - 1]
    mid_index = len(input_list) // 2

    if number == end_value:
        return len(input_list) - 1

    mid_index = recursive_rotate_search(mid_index, end_value)

    if number > end_value:

        search = recursive_binary_search(number, input_list[:mid_index + 1])

        return search

    if number < end_value:

        search = recursive_binary_search(number, input_list[mid_index + 1:])

        return search + len(input_list[:mid_index]) + 1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
    print("____")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25, 26, 27, 28, 29, 1, 2, 3, 4, 5], 4])
test_function([[18, 19, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 17])