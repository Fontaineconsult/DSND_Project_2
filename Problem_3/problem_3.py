

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    return_list = ['','']
    location = 0

    for number in range(len(input_list) -1, 0, -1):
        # bubble sort
        for i in range(number):

            if input_list[i] < input_list[i+1]:

                temp = input_list[i]

                input_list[i] = input_list[i+1]

                input_list[i+1] = temp



    for each in input_list:

        if location == 0:
            return_list[0] = return_list[0] + str(each)

        if location == 1:
            return_list[1] = return_list[1] + str(each)

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