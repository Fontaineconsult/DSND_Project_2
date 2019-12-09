
def min_max(ints):

    stack_min = ints[0]
    stack_max = ints[0]

    for int in ints[1:]:

        if int < stack_min:
            stack_min = int
        if int > stack_max:
            stack_max = int

    return (stack_min, stack_max)


import random


# Test 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == min_max(l)) else "Fail")


# Test 2
l = [i for i in range(0, 1532)]  # a list containing 0 - 1531
random.shuffle(l)

print ("Pass" if ((0, 1531) == min_max(l)) else "Fail")


# Test 3
l = [i for i in range(0, 2)]  # a list containing 0 - 1
random.shuffle(l)

print ("Pass" if ((0, 1) == min_max(l)) else "Fail")
