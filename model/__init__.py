#!/usr/bin/python
# -*- coding: utf-8 -*-


class Room:

    def __init__(self, items=None, name=[]):

        self.items = items
        if len(items):
            self.items_str = ', '.join(items)
        else:
            self.items_str = 'This room is empty.'
        self.name = name


class Rooms:

    class A(Room):

        def __init__(self):
            items = []
            name = 'A'

            Room.__init__(self, items, name)

    class B(Room):

        def __init__(self):
            items = ['TV', 'DVD', 'WIFI-Router', 'Ipad', 'Chair']
            name = 'B'

            Room.__init__(self, items, name)

    class C(Room):

        def __init__(self):
            items = ['key', 'table']
            name = 'C'

            Room.__init__(self, items, name)

    class D(Room):

        def __init__(self):
            items = ['piano', 'sofa', 'chair']
            name = 'D'

            Room.__init__(self, items, name)

    class E(Room):

        def __init__(self):
            items = ['$1000000', 'Cake']
            name = 'E'

            Room.__init__(self, items, name)


class CommandParameter:

    def __init__(self, command):
        self.command = command

    def getParams(self):

        if self.command == 'go':
            return ', '.join(['w', 'e', 's', 'n'])

        if self.command == 'get':
            return 'itemName'


class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
