Problem 1 utilizes a simple recursive function.
 Recursion is the clear winner with this problem as we don't know
 how many times we will need call the function to zero-in on the
 answer. 
 
 Each time we call the function we check if multiplying the number we are
 checking by a guess number and the dividing that product by the number yields 
 a number between 0 and 1. If greater or less than 0 and 1 we call the function
 again. Eventually the guess number will be within 0 and 1 of the square root.
 We return the floor of the guess.
 
Time complexity is O(Log N). 
