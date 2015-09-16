#!/usr/bin/python
# -*- coding: utf-8 -*-
import shlex
import sys

import readline  # this will allow arrow up and down for shell

from helpers import Draw, Help, Navigation
from model import Rooms, CommandParameter, bcolors


class Game():

    def run(self):

        draw = Draw()

        print draw.map()

        rooms = Rooms()
        current_room = rooms.A()
        items = ''
        hasKey = 0
        picked_items = []
        unlocked = 0

        commands = ['quit', 'help', 'mission', 'items']
        room_commands = ['go', 'location', 'look', 'get', 'unlock']
        h = Help()

        while 1:
            try:
                Decisionst = raw_input('>>  ')
                command = shlex.split(Decisionst)

                if command[0] in commands:

                    if command[0] == 'help':

                        print h.help()
                    elif command[0] == 'quit':

                        print 'bye, bye'
                        sys.exit()
                    elif command[0] == 'mission':

                        h = Help()
                        print h.objective()
                    elif command[0] == 'items':

                        if len(picked_items):
                            print 'You are taking with you this items: ' \
                                  + ', '.join(picked_items)
                        else:
                            print 'Your bag has no items in it.'
                    else:
                        print bcolors.FAIL \
                              + 'Command not found, Please use help to list commands.' \
                              + bcolors.ENDC
                else:

                    if command[0] in room_commands:

                        if len(command) > 1:

                            if command[0] == 'go':
                                current_room = Navigation(command[1], current_room.name, hasKey).getRoom()

                                if current_room:
                                    print 'Welcome to room: ' \
                                          + current_room.name

                                    if hasKey and current_room.name == 'A':
                                        if unlocked == 0:
                                            print 'You got a key. Unlock room E.'

                                    items = current_room.items

                                    if 'key' in items:
                                        print 'Maybe you want to look at current room :)'

                            if command[0] == 'get':
                                options = ['key']
                                if command[1] in options and command[1] in picked_items:
                                    hasKey = 1
                                    print 'You got a key. Go now and unlock room E'
                                else:

                                    if command[1] in items:

                                        if command[1] not in picked_items:
                                            picked_items.append(command[1])

                                            if command[1] == 'key':

                                                print 'You got a key. Go now and unlock room E'
                                                hasKey = 1
                                            else:
                                                print 'You get ' + command[1] + '. Good for you'
                                    else:
                                        print 'There is no such item in this room'
                        else:

                            if command[0] == 'location':

                                print 'You are in room: ' + current_room.name
                            elif command[0] == 'look':

                                print 'Room items: ' + current_room.items_str
                            elif command[0] == 'unlock':

                                if hasKey and current_room.name == 'A':
                                    unlocked = 1
                                    print bcolors.OKGREEN \
                                          + 'GREAT. Mission accomplished. Room E is unlock. Enter room E.' \
                                          + bcolors.ENDC
                                else:
                                    if current_room.name != 'A':
                                        print bcolors.OKGREEN \
                                              + 'You can not unlock room E from ' \
                                              + current_room.name + bcolors.ENDC
                                    else:
                                        print 'You do not have key. Tip: it is in room C.'
                            else:

                                c = CommandParameter(command[0])
                                print bcolors.FAIL \
                                      + 'Command is missing parameters' \
                                      + bcolors.ENDC
                                print 'This params are available for command ' \
                                      + command[0] + ':\n'
                                print '    ' + c.getParams()
                    else:

                        print bcolors.FAIL \
                              + 'Command not found, Please use help to list commands.' \
                              + bcolors.ENDC

            except KeyboardInterrupt:
                print bcolors.OKGREEN+"Goodbye!"+bcolors.ENDC
                sys.exit()
