import sys, os

from curses import wrapper
from CursesApp import CursesApp
from TM import TM




def main(stdscr):
    stdscr.clear()
    app = CursesApp(stdscr, tm)



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Not enough arguments given!')
        print('Usage: python ' + sys.argv[0] + ' <program file>')
        sys.exit()

    path = sys.argv[1]

    if not os.path.exists(path) :
        print(f'File not found : "{path}"')
        sys.exit()

    tm = TM(path)

    wrapper(main)
