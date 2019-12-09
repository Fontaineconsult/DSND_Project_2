

def sqrt_recursive(target, guess):


    if guess ** 2 - target >= 0 and guess ** 2 - target <= 1.0:

        return guess // 1

    new_guess = (guess + target / guess) / 2

    return sqrt_recursive(target, new_guess)



def sqrt(num):

    if num < 1:
        return 0
    return sqrt_recursive(num, 1)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (100 == sqrt(10000)) else "Fail")