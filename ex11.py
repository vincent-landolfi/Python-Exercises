from container import *


def banana_game(s1, s2, c):
    ''' (str,str,Container) -> bool
    Returns true iff you can turn s1 into s2
    using c given the rules provided in the
    ex2 handout
    '''
    # copy the container so it doesnt mutate
    c = c.copy()
    # check if the two words are the same and
    # the container is empty
    if s1 == '' and s2 == '' and c.is_empty():
        # then its true
        result = True
    # check if the container is not empty but the strings
    # are
    elif s1 == '' and s2 == '' and not c.is_empty():
        # then its false
        result = False
    # if they arent
    else:
        # check if both first letters are the same
        if (s1 != '' and s2 != '') and (s1[0] == s2[0]):
            # cut the first letter out of both,
            # try again
            result = banana_game(s1[1:], s2[1:], c)
        # if theyre not the same
        # peek at the next letter, see if we
        # can use it
        elif (not c.is_empty()) and (c.peek() == s2[0]):
            # get the value
            c.get()
            # cut out the first value from s2
            result = banana_game(s1, s2[1:], c)
        # check if the two first values arent the same
        elif (s1 != '' and s2 != '') and (s1[0] != s2[0]):
            # try to put it in
            try:
                # then put it in the container
                c.put(s1[0])
                # cut out first value from s1
                result = banana_game(s1[1:], s2, c)
            # if we cant then it wont work
            except:
                result = False
        else:
            result = False
    return result
