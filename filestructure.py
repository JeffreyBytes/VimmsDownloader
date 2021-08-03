import os
import sys
from typing import List

selections: list[dict[int, str]] = [
    {0: 'NES'},
    {1: 'Genesis'},
    {2: 'SNES'},
    {3: 'Saturn'},
    {4: 'Playstation'},
    {5: 'N64'},
    {6: 'Dreamcast'},
    {7: 'Playstation-2'},
    {8: 'Xbox'},
    {9: 'Gamecube'},
    {10: 'Playstation-3'},
    {11: 'Wii'},
    {12: 'WiiWare'},
    {13: 'Game-Boy'},
    {14: 'Game-Boy-Color'},
    {15: 'Game-Boy-Advanced'},
    {16: 'Nintendo-DS'},
    {17: 'PSP'},
]


class __Config:
    def __init__(self, Selections: List[str] = [], All: bool = False, Extract: bool = False, Search: bool = False, Bulk: bool = False):
        self.Selections = Selections
        self.All = All
        self.Extract = Extract
        self.Search = Search
        self.Bulk = Bulk


def __CreateAlphaNumStructure(path: str, system: str):
    dirnames: list[str] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    try:
        for x in dirnames:
            os.mkdir(os.path.join(path, 'ROMS', system, x))
    except:
        e = sys.exc_info()[0]
        print('Failed Creating AlphaNum Structure')
        print(e)


def __CreateROMHomeDir(path: str):
    try:
        os.mkdir(os.path.join(path, 'ROMS'))
    except:
        e = sys.exc_info()[0]
        print('Failed Creating Home Directory')
        print(e)


def __CreateROMSystemDir(path: str, system: str):
    try:
        os.mkdir(os.path.join(path, 'ROMS', system))
    except:
        e = sys.exc_info()[0]
        print('Failed Creating ROM System Directory')
        print(e)


def __CheckIfHomeDirCreated(path: str):
    for x in os.listdir(path):
        if x == 'ROMS':
            return True


def __CheckIfSystemDirCreated(path: str, system: str):
    for x in os.listdir(os.path.join(path, 'ROMS')):
        if x == system:
            return True


def __CreateAllNoHome(path):
    __CreateROMHomeDir(path)
    for x in selections:
        for value in x:
            if not __CheckIfSystemDirCreated(path, x[value]):
                __CreateROMSystemDir(path, x[value])
                __CreateAlphaNumStructure(path, x[value])


def __CreateAllWHome(path):
    for x in selections:
        for value in x:
            if not __CheckIfSystemDirCreated(path, x[value]):
                __CreateROMSystemDir(path, x[value])
                __CreateAlphaNumStructure(path, x[value])


def __CreateSelWHome(path, userselections: List[str]):
    for x in userselections:
        if not __CheckIfSystemDirCreated(path, selections[int(x)][int(x)]):
            __CreateROMSystemDir(path, selections[int(x)][int(x)])
            __CreateAlphaNumStructure(path, selections[int(x)][int(x)])


def __CreateSelNoHome(path, userselections: List[str]):
    __CreateROMHomeDir(path)
    for x in userselections:
        if not __CheckIfSystemDirCreated(path, selections[int(x)][int(x)]):
            __CreateROMSystemDir(path, selections[int(x)][int(x)])
            __CreateAlphaNumStructure(path, selections[int(x)][int(x)])


def CreateDirectoryStructure(config: __Config):
    path: str = os.getcwd()
    if config.All:
        if not __CheckIfHomeDirCreated(path):
            __CreateAllNoHome(path)
        if __CheckIfHomeDirCreated(path):
            __CreateAllWHome(path)
    if not config.All:
        if not __CheckIfHomeDirCreated(path):
            __CreateSelNoHome(path, config.Selections)
        if __CheckIfHomeDirCreated(path):
            __CreateSelWHome(path, config.Selections)
