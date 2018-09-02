class LightSwitch():
    " A switch that can be turned on or off"

    def __init__(self, mode):
        ''' (LightSwitch,bool) -> NoneType
        Creates a new light switch that is either
        on or off
        REQ: mode in {'on','off'}
        '''
        # check if mode is set to on
        if (mode == 'on'):
            # set class variable to on
            self._is_on = True
        # check if mode is set to off
        elif (mode == 'off'):
            # set class variable to off
            self._is_on = False

    def turn_on(self):
        ''' (LightSwitch) -> NoneType
        Turns light switch on
        '''
        # light is on to True
        self._is_on = True

    def turn_off(self):
        ''' (LightSwitch) -> NoneType
        Turns light switch off
        '''
        # light is on to False
        self._is_on = False

    def flip(self):
        ''' (LightSwitch) -> NoneType
        Flips the switch to either off or on
        depending on where the switch currently is
        '''
        # change if the light is on to the opposite
        self._is_on = not(self._is_on)

    def __str__(self):
        ''' (Lightswitch) -> str
        Makes string saying whether switch is on
        or off
        '''
        # check if light is on
        if (self._is_on):
            # variable for on or off is on
            on_off = "on"
        else:
            # variable for on or off is off
            on_off = "off"
        return ("I am " + on_off)


class SwitchBoard():
    " Switchboard full of switch that are on/off"

    def __init__(self, num_switches):
        '''(SwitchBoard,int) -> NoneType
        Creates a new switch board with
        num_switches number if switches
        REQ: num_switches>0
        '''
        # set the class variable to given
        self._switches = num_switches
        # make an empty list for switches
        self._switch_list = []
        # create the switches, in a list
        for i in range(0, self._switches):
            # append new switch to switch list
            self._switch_list.append(LightSwitch('off'))

    def __str__(self):
        '''(SwitchBoard) -> str
        Makes string telling which switches
        are on
        '''
        # make a string using the list from which switch
        on_string = ' '.join(str(e) for e in self.which_switch())
        # return the proper string
        return "The following switches are on: " + on_string

    def which_switch(self):
        '''(SwitchBoard) -> list
        Return a list of which switches are
        on in order
        '''
        # make a blank list
        self._on_list = []
        # go through all the switches
        for i in self._switch_list:
            # check which are on
            if (i.__str__() == "I am on"):
                # add it to the on list
                self._on_list.append(self._switch_list.index(i))
        # return the list of switchs that are on
        return self._on_list

    def flip(self, index):
        '''(SwitchBoard,int) -> NoneType
        Flips the switch at the given index
        REQ: 0 < index < len(switch_list)
        '''
        # check if the switch exists
        if (index < self._switches):
            # flip the switch
            (self._switch_list[index]).flip()

    def flip_every(self, multiple):
        '''(SwitchBoard,int) -> NoneType
        Flips the switch at every multiple
        of the given number
        REQ: multiple > 0
        '''
        # create number that we'll be using each time
        flip_num = 0
        # while loop making sure we're less than number of switches
        while(flip_num < self._switches):
            # flip the switch at that index
            self._switch_list[flip_num].flip()
            # add our multiple
            flip_num += multiple

    def reset(self):
        '''(SwitchBoard) -> NoneType
        Turns all the switches off
        '''
        # go through each switch
        for i in self._switch_list:
            # turn the switch off
            i.turn_off()
            
    def get_switches(self):
        '''(SwitchBoard) -> int
        Returns the number of switches
        '''
        return self._switches

if (__name__ == "__main__"):
    # make switch board with 1024 switches
    test = SwitchBoard(1024)
    # do flip_every, incrementing by 1
    for i in range(1, test.get_switches()):
        test.flip_every(i)
    print(test)
