#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config(object):
    def __init__(self):
        self.number_of_decisions = 37
        self.number_of_states = 1

        # A list of all configs defined for every single state.
        self.states_configs = ['state', 'letters', 'actions', 'letters_solver', 'actions_solver']

        # A list of all configs defined as globals,
        # not assigned to any particular state.
        self.other_configs = []

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!! Only keys defined in states_configs and other_configs 
        # will be visible in your application.!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # States transition matrix
        self.state = [self.number_of_decisions * [0]]

        # Graphics definition for every state. Normally for every state it should be a collection of strings.
        # Hovewever, sometimes we have a collection of strings, not a single string. It happens when we have a 'dynamic' state.
        # In that case there should be a corresponding graphics_solver variable with method that resolves graphics definition at runtime.
        self.letters = [["A", "O", "N", "T", "D", "J",
                       "G", u"Ó", "I", "Z", "S", "K",
                       "U", "B", u"Ą", u"Ć", "E", "W",
                       "Y", "M", u"Ł", "H", u"Ś", u"Ń",
                       "R", "C", "P", "L", u"Ę", u"Ż",
                       "F", u"Ź", "POWIEDZ", u"USUŃ", "SPACJA", "ZNAKI", u"WYJDŹ"]]

        # See descripton above.
        self.letters_solver = [[""]*self.number_of_decisions]

        # actions[i][j] will be performed in state i when person is looking on square j
        # If you wish no action - leave it empty.
        # If you have a 'dynamic' state and you want the program to be chosen at runtime, set here a collection of programs - 
        # thanks to corresponding values from actions_solver obci will decide which program to use.
        self.actions = [["msg('A')", "msg('O')", "msg('N')", "msg('T')", "msg('D')", "msg('J')", 
                      "msg('G')", "msg(u'Ó')", "msg('I')", "msg('Z')", "msg('S')", "msg('K')", 
                      "msg('U')", "msg('B')", "msg(u'Ą')", "msg(u'Ć')", "msg(u'Ę')", "msg('W')",
                      "msg('Y')", "msg('M')", "msg(u'Ł')", "msg('H')", "msg(u'Ś')", "msg(u'Ń')",
                      "msg('R')", "msg('C')", "msg('P')", "msg('L')", "msg(u'Ę')", "msg(u'Ż')",
                      "msg('F')", "msg(u'Ź')", "msg('nic0')", "backspace(2)", "msg(' ')", "msg('nic')","msg(nic2)"]]
    
    

        # See description above.
        self.actions_solver = [[""]*self.number_of_decisions]

    def _finish_action(self):
        return "finish()"
