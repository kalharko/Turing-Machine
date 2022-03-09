import sys, os

from unicurses import *
from CursesApp import CursesApp
from TM import TM




if __name__ == '__main__':
    # Args
    if len(sys.argv) < 2:
        print('Not enough arguments given!')
        print('Usage: python ' + sys.argv[0] + ' <program file>')
        sys.exit()

    path = sys.argv[1]

    if not os.path.exists(path) :
        print(f'File not found : "{path}"')
        sys.exit()

    # Turing Machine
    tm = TM(path)

    # curses initialization
    stdscr = initscr()
    noecho()
    cbreak()
    curs_set(0)

    # CursesApp launch
    app = CursesApp(stdscr, tm)

    curs_set(1)
    nocbreak()
