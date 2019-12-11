
def sort_012(input_list):

    if len(input_list) == 0:
        return []




    start = 0
    mid = 0
    mid_value = 1
    end = len(input_list) - 1

    while mid <= end:

        if input_list[mid] < mid_value:

            value = input_list[start]
            input_list[start] = input_list[mid]
            input_list[mid] = value
            start += 1
            mid += 1

        elif input_list[mid] > mid_value:

            value = input_list[mid]
            input_list[mid] = input_list[end]
            input_list[end] = value
            end -= 1

        else:
            mid += 1
    print(input_list)
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):

        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 2, 1, 1, 1, 2, 2])
test_function([])