def copy_me (input_list):
    ''' (list) -> list
    Return a list where all the strings from the original lists
    are capitalized, all the ints and floats have their value
    increased by 1, booleans negated, and lists are replaced with
    the word 'List', but in a new list
    >>> copy_me(['hello',[1,2],1,1.0,False])
    ['HELLO','List',2,2.0,True]
    >>> copy_me ([True])
    [False]
    >>> copy_me([{1,2,3},4])
    [{1,2,3},5]
    '''
    # instantiate output list
    output_list = []
    # traverseinput list
    for i in range (0,len(input_list)):
        #see what type each element is
        #string case
        if (type(input_list[i]) == str):
            # capitalize string, add to output list
            output_list.append(input_list[i].upper())
        # int and float case
        elif (type(input_list[i]) == int or type(input_list[i]) == float):
            # increase value by 1, add to output list
            output_list.append(input_list[i]+1)
        elif (type(input_list[i]) == bool):
            # negate value, add to output list
            output_list.append(not(input_list[i]))
        elif (type(input_list[i]) == list):
            # change to word 'List', add to output list
            output_list.append('List')
        # any other type
        else:
            # just add it to the list
            output_list.append(input_list[i])
    # return the new list we made
    return output_list

def mutate_me(input_list):
    ''' (list) -> NoneType
    Return a list where all the strings from the original lists
    are capitalized, all the ints and floats have their value
    increased by 1, booleans negated, and lists are replaced with
    the word 'List', but by mutating input list
    >>> copy_me(['hello',[1,2],1,1.0,False])
    ['HELLO','List',2,2.0,True]
    >>> copy_me ([True])
    [False]
    >>> copy_me([{1,2,3},4])
    [{1,2,3},5]
    '''
    # traverse input list
    for i in range (0,len(input_list)):
        #see what type each element is
        #string case
        if (type(input_list[i]) == str):
            # capitalize string, mutate list
            input_list[i] = (input_list[i].upper())
        # int and float case
        elif (type(input_list[i]) == int or type(input_list[i]) == float):
            # increase value by 1, mutate list
            input_list[i] = (input_list[i]+1)
        elif (type(input_list[i]) == bool):
            # negate value, mutate list
            input_list[i] = (not(input_list[i]))
        elif (type(input_list[i]) == list):
            # change to word 'List', add to output list
            input_list[i] = ('List')
        # any other type  