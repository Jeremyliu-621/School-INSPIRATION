"""

Palindrome maker - practise with lists. No reversed() allowed

palindrome.py
Jeremy liu
4/2/2025

"""

def main():

    numbers = input("Give me single-digit numbers seperated by commas and a space (', '): ").replace(" ", "").split(",")
    
    numbers_reversed = reverser(numbers, len(numbers)-1) # gets a reversed list
    
    numbers.pop() # already pops last element
    for element in numbers_reversed:
        numbers.append(element)
    
    numbers_str = ", ".join(numbers)
    print(f"Your list in palindrome format is:\n{numbers_str}")

def reverser(numbers, last_index):

    if last_index < 0:
        return []
    else:
        """
        numbers[index] is a single element (a string, since split() returns a list of strings).

        If you just wrote numbers[index] + reverser(numbers, index - 1), Python would try to concatenate 
        a string with a list, which would cause a TypeError.

        Wrapping numbers[index] in square brackets ([numbers[index]]) turns it into a single-element list, 
        which can be concatenated with another list (reverser(numbers, index - 1)).
        """
        return [numbers[last_index]] + reverser(numbers, last_index - 1) # reverser does not need square brackets because we are passing in parameters

        # take numbers = ['1', '3', '5']
        # in this specific code, the return statement:
        # returns the last element ([numbers, len(numbers)-1]) in numbers, '5'
        # and also the number before it, (numbers[len(numbers)-1 - 1])
        
main()