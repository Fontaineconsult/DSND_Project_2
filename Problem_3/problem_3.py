def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):

    return_list = ['','']
    location = 0

    input_list = mergesort(input_list)
    print(input_list)



    for each in range( len(input_list) -1, -1, -1):

        if location == 0:
            return_list[0] = return_list[0] + str(input_list[each])

        if location == 1:
            return_list[1] = return_list[1] + str(input_list[each])

        # swtich back and forth for each return number
        location = 1 if location == 0 else 0


    return_list[0] = int(return_list[0])
    return_list[1] = int(return_list[1])

    return return_list



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")



test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[7, 4, 8, 1, 2, 0], [841, 720]])
test_function([[0, 0], [0, 0]])