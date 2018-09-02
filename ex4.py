def insert(first_list, second_list, index):
    ''' (str or list, str or list) -> str or list
    Return a list with the second list added to the first list at the
    given idex iff both parameters are lists. Otherwise, do the same
    but in a string instead of a list.
    REQ: index must be int
    >>> insert([1, 2, 3], ['a', 'b', 'c'], 2)
    [1, 2, 'a', 'b', 'c', 3]
    >>> insert("123","abc",2)
    '12abc3'
    '''
    # return the first list, sliced up to the index
    # then add the entire second list
    # finally add the rest of the first list to the return
    return (first_list[0:index] + second_list[0:len(second_list)] +
            first_list[index:len(first_list)])


def up_to_first(given_list, obj):
    ''' (list or str, obj) -> list or str
    Return the given list rewritten up to the first occurrence
    of the given obj. Otherwise do the same but with a string.
    >>> up_to_first([1, 2, 3, 4], 3)
    [1, 2]
    >>> up_to_first([1, 2, 3, 4], 9)
    [1, 2, 3, 4]
    >>> up_to_first('1234','3')
    '12'
    >>> up_to_first('afvgb','v')
    'af'
    '''
    # check if object is in the list
    if (obj in given_list):
        # slice list up to the index that the object is
        up_to_list = given_list[0:given_list.index(obj)]
    else:
        # just return the list unchanged
        up_to_list = given_list
    return up_to_list


def cut_list(given_list, index):
    ''' (list,int) -> list
    Return the given list, with the letters before the given index
    put after the index, and the letters after the index put before
    the index
    REQ: index is inside the list
    >>> cut_list([0,1,2,3,4,5,6,7,8,9], 3)
    [4, 5, 6, 7, 8, 9, 3, 0, 1, 2]
    >>> cut_list("ABCDEFGX1234",7)
    '1234XABCDEFG'
    '''
    # return the given list from the index on
    # then add the object at the index
    # and finally add the beginning portion of the list
    return (given_list[index + 1:len(given_list)] +
            given_list[index:index + 1] + given_list[0:index])
