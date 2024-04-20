#! /usr/bin/env python3
""" 
    the nth_most_rate_signature is a function that returns the nth-rarest item given to the function
    it is supplied with two arguments, list of arrays/list of integers and n is for number of times the given integer appeared in the list.
    E.G [5,4,5,4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5] if 5 is supplied as n it will return, the answer is 5 as 5 is the 5th rarest item
"""


def nth_most_rate_signature(my_list=[], nums=''):
    # create an empty list to host the new list 
    new_list = []
    
    # looping through the list
    for num in my_list:
        
        # checking if number supplied is in the list
        if nums not in my_list:
            return f"Sorry {nums} is not in the list"
        # checking if the given argument nums is contained in the new list num
        if num == nums:
           new_list.append(num)
      
    # checking which output will be displayed depending on the input given to the function
         
    if len(new_list) == 1:
        return f"the answer is {nums} as {nums} is the {len(new_list)}st rarest item"
    elif len(new_list) == 2:
        return f"the answer is {nums} as {nums} is the {len(new_list)}nd rarest item"
    elif len(new_list) == 3:
         return f"the answer is {nums} as {nums} is the {len(new_list)}rd rarest item"
    else:
        return f"the answer is {nums} as {nums} is the {len(new_list)}th rarest item"

# invoking the nth_most_rate_signature 
while True:
    user_input = input('input your search number ')
    if user_input == 'stop':
        break
    print(nth_most_rate_signature([5,4,5,4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5], int(user_input)))
