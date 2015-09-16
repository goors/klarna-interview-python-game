#!/usr/bin/python
# -*- coding: utf-8 -*-
from model import Rooms, bcolors


class Draw:

    def map(self):
        line = '  _________ \n'
        line += '|         |\n'
        line += '|         |\n'
        line += '| Room E  |\n'
        line += '|         |\n'
        line += '|         |\n'
        line += '|____?____|_________\n'
        line += '|         |         |\n'
        line += '|         |         |\n'
        line += '|         |         |\n'
        line += '| Room A  = Room B  |\n'
        line += '|         |         |\n'
        line += '|___||____|____||___|\n'
        line += '|         |         |\n'
        line += '|         |         |\n'
        line += '|         |         |\n'
        line += '| Room D  =  Room C |\n'
        line += '|         |         |\n'
        line += '|_________|_________|\n'
        line += 'Welcome to my Text Adventure!\n'
        line += "Use the 'help' command for help!"
        return line





class Help:

    def help(self):
        line = '    \n    You can use the following commands:\n\n'
        line += '    '+bcolors.HEADER+'go'+bcolors.ENDC+' n,s,w,e\n'
        line += '    '+bcolors.HEADER+'location'+bcolors.ENDC+' - prints room you\'re in\n'
        line += '    '+bcolors.HEADER+'look'+bcolors.ENDC+' - show current room itmes\n'
        line += '    '+bcolors.HEADER+'get item'+bcolors.ENDC+' - pick some item from room\n'
        line += '    '+bcolors.HEADER+'unlock'+bcolors.ENDC+' - unlock sealed room\n'
        line += '    '+bcolors.HEADER+'mission'+bcolors.ENDC+' - mission objective\n'
        line += '    '+bcolors.HEADER+'items'+bcolors.ENDC+' - your current items list\n'
        line += '    '+bcolors.HEADER+'quit'+bcolors.ENDC+'\n'
        line += '    ''\n'
        line += '    You can exit Game anytime by pressing '+bcolors.HEADER+'Ctrl+c'+bcolors.ENDC+'.\n'
        line += '    You can use '+bcolors.HEADER+'Up'+bcolors.ENDC+' and '+bcolors.HEADER+'Down'+bcolors.ENDC+' arrow keys like in Linux console to get prev/next line.\n'

        return line

    def objective(self):
        d = \
            '''    
    Misson objective is to open room E with key from room C.
'''
        d += '    You are starting from room A.\n'
        return d


class Navigation:

    def __init__(
        self,
        where,
        current_room,
        hasKey=0,
        ):

        self.directions = ['w', 's', 'n', 'e']
        self.current_room = current_room
        self.where = where
        self.has_key = hasKey

    def getRoom(self):


        rooms = Rooms()
        available = {

            "A":{
                "directions" : {
                    "n":rooms.E(),
                    "e":rooms.B(),
                    "s":rooms.D()
                },
                "A": rooms.A()
            },
            "B":{
                "directions" : {
                    "w":rooms.A(),
                    "s":rooms.C()
                }
                ,
                "B": rooms.B()
            },
            "C":{
                "directions" : {
                    "n":rooms.B(),
                    "w":rooms.D()
                },
                "C": rooms.C()

            },
            "D":{
                "directions" : {
                    "n":rooms.A(),
                    "e":rooms.C()
                },
                "D": rooms.D()
            },
            "E":{
                "directions" : {
                    "s":rooms.A()

                },
                "E": rooms.E()
            }

        }

        error = "You can not go there. Go the other way."


        if self.where not in available[self.current_room]["directions"] or self.where not in self.directions:
            print error
            return available[self.current_room][self.current_room]

        else:
            if self.has_key == 0 and self.current_room == "A" and self.where == "n":
                print "You do not have key to enter this room."
                return rooms.A()

            return available[self.current_room]["directions"][self.where]