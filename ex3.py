def percent_to_gpv(mark):
    ''' (int) -> float
    Returns a float grade point value corresponding to the given percentage
    mark.
    REQ: 0<=mark<=100
    >>> percentage_to_gpv(86)
    4.0
    >>> percentage_to_gpv(81)
    3.7
    >>> percentage_to_gpv(78)
    3.3
    >>> percentage_to_gpv(75)
    3.0
    >>> percentage_to_gpv(71)
    2.7
    >>> percentage_to_gpv(68)
    2.3
    >>> percentage_to_gpv(64)
    2.0
    >>> percentage_to_gpv(61)
    1.7
    >>> percentage_to_gpv(58)
    1.3
    >>> percentage_to_gpv(54)
    1.0
    >>> percentage_to_gpv(51)
    0.7
    >>> percentage_to_gpv(35)
    0.0
    '''
    # go through all possibilities, convert to gpv
    if (mark>=85 and mark<=100):
        gpv = 4.0
    elif (mark>=80 and mark<=84):
        gpv = 3.7
    elif (mark>=77 and mark<=79):
        gpv = 3.3
    elif (mark>=73 and mark<=76):
        gpv = 3.0
    elif (mark>=70 and mark<=72):
        gpv = 2.7
    elif (mark>=67 and mark<=69):
        gpv = 2.3
    elif (mark>=63 and mark<=66):
        gpv = 2.0
    elif (mark>=60 and mark<=62):
        gpv = 1.7
    elif (mark>=57 and mark<=59):
        gpv = 1.3
    elif (mark>=53 and mark<=56):
        gpv = 1.0
    elif (mark>=50 and mark<=52):
        gpv = 0.7
    elif (mark>=0 and mark<=49):
        gpv = 0
    #return the gpv
    return gpv

def card_namer(value,suit):
    ''' (str or int,str) -> str
    Returns the name of the card from the standard deck, given the value of
    the card, and the suit
    REQ: value in {A,2,3,4,5,6,7,8,9,T,J,Q,K}
    REQ: suit in {D,C,H,S}
    >>> card_namer('Q','D')
    'Queen of Diamonds'
    >>> card_namer('9','S')
    '9 of Spades'
    >>> card_namer('8','T')
    'CHEATER!'
    '''
    # go through letter possibilities
    if (value == 'A'):
        name = 'Ace of '
    elif (value == 'T'):
        name = '10 of '
    elif (value == 'J'):
        name = 'Jack of '
    elif (value == 'Q'):
        name = 'Queen of '
    elif (value == 'K'):
        name = 'King of '
    # otherwise, its a number, leave it
    else:
        name = value + ' of '
    #check the suit, assign to corresponding string        
    if (suit == 'D'):
        suit_name = 'Diamonds'
    elif (suit == 'C'):
        suit_name = 'Clubs'
    elif (suit == 'H'):
        suit_name == 'Hearts'
    elif (suit == 'S'):
        suit_name = 'Spades'
    # otherwise its not it the required list
    else:
        name = ''
        suit_name = 'CHEATER!'
    # return the two full strings concatenated
    return (name + suit_name)

def my_str(obj):
    '''(obj) -> str
    Returns different strings based on the type of the object inputted. Strings
    are just returned as is. Booleans get returned "YES" for True and "NO" for
    false. If the object is an integer, anything <= 10 will return "Small 
    Number", 11-99 returns "Medium Number", any larger will return "Large 
    Number". If the object is a float, it will be returned as a string,
    rounded to at most 2 decimal places. Any other data type will return "I 
    dunno"
    REQ: ----
    >>> my_str("Hello")
    'Hello'
    >>> my_str(False)
    'NO'
    >>> my_str(42)
    'Medium Number'
    >>> my_str(42.0)
    '42.0'
    >>> my_str(3.1415926)
    '3.14'
    >>> my_str([1, 2, 3])
    'I dunno'
    '''
    #cover string case
    if (type(obj) == str):
        rep = obj
    #cover boolean case
    elif (type(obj) == bool):
        if (obj):
            rep = 'YES'
        else:
            rep = 'NO'
    #cover integer case
    elif (type(obj) == int):
        if (obj<=11):
            rep = 'Small Number'
        elif (obj>11 and obj<=99):
            rep = 'Medium Number'
        else:
            rep = 'Large Number'
    #cover float case
    elif (type(obj) == float):
        rep = str(round(obj,2))
    else:
        rep = 'I dunno'
    #return the representation value
    return rep