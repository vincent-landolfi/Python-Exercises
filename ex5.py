def function_names(filename):
    ''' (io.TextIOWrapper) -> list of str
    Return a list of all the names of
    functions in the given file.
    REQ: file is in same folder as this file
    >>> function_names("ex4.py")
    ['insert','up_to_first','cut_list']
    >>> function_names("ex3.py")
    ['percent_to_gpv','card_namer','.y_str']
    >>> function_names('essay.txt')
    []
    '''
    # instantiate the list we'll be returning
    name_list = []
    # open file for reading
    filehandle = open(filename, 'r')
    # use the readlines function to get list of each line
    func_list = filehandle.readlines()
    # for loop going through each line of file
    for i in range(0, len(func_list)):
        # check if the line starts with 'def'
        if (func_list[i].startswith('def')):
            # add string to list we are returning, by going from
            # 4 letters after 'def', which is where the name of
            # the function starts, up to where it finds the first
            # brackets for parameters, giving the function name fully
            name_list.append(func_list[i][4:func_list[i].find('(')])
    # close filehandle, not because we need to but good practice
    filehandle.close()
    # return the list we made with the function names
    return name_list


def justified(filename):
    ''' (io.TextIOWrapper) -> bool
    Return True iff each line in the file
    is left-justified
    >>> justified("ex5_just_all_left.txt")
    False
    >>> justified("ex5_just_not_left.txt")
    True
    '''
    # instantiate boolean we'll be returning, counter int,
    # and the list we'll be reading the lines to
    left_justified = True
    counter = 0
    lines_list = []
    # open file for reading
    filehandle = open(filename, 'r')
    # use readlines to write each line to a list
    lines_list = filehandle.readlines()
    # while loop, runs while either it hasnt searched all the line
    # or it finds a line with a space at the start
    while ((counter < len(lines_list)) and left_justified):
        # check if line starts with a space
        if (lines_list[counter].startswith(' ')):
            left_justified = False
        # raise the counter
        counter += 1
    # return if it is left justified
    return left_justified


def section_average(filename, section_code):
    ''' (io.TextIOWrapper,str) -> float
    Return the average midterm for all students in a section,
    given the grade file for the course, and the code for the
    section
    >>> section_average('ex5_grade_file.txt','LEC01')
    17.25
    >>> section_average('ex5_grade_file.txt','LEC02')
    18.25
    >>> section_average('ex5_grade_file.txt','LEC30')
    12.25
    '''
    # instatiate two floats for average and list for reading
    average = 0.0
    num_in_section = 0.0
    lines_list = []
    # open file for reading
    filehandle = open(filename, 'r')
    # use readlines to write each line to our list
    lines_list = filehandle.readlines()
    # for loop going through all the lines
    for i in range(0, len(lines_list)):
        # split the list to another one
        section_list = lines_list[i].split()
        # for loop going through the section list
        for j in range(0, len(section_list)):
            # check if the person is in the section
            if (section_list[j] == section_code):
                # add mark to the total
                average += float(section_list[j + 1])
                # add one to the number of people in that section
                num_in_section += 1
    # check if that section was actually there
    if (average == 0.0):
        # make average a none value
        average = None
    else:
        # do the average calculation
        average = (average / num_in_section)
    return average
