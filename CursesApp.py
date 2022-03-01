import curses, os, shutil, locale, random

from TM import TM


class CursesApp() :
    def __init__(self, stdscr, tm):
        self.tm = tm

        # encoding
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        self.code = locale.getpreferredencoding()
        curses.curs_set(0)

        # constants
        self.ESCAPE = ['q']

        self.screen = stdscr
        self.screenH, self.screenW = self.screen.getmaxyx()
        self.tapeH = self.screenH//2 + 1
        self.screen.refresh()

        curses.init_pair(1, 0,255)
        self.mainLoop()


    def mainLoop(self) :
        self.display()
        user_input = self.screen.get_wch()

        while not user_input in self.ESCAPE :
            if user_input == 'r' :
                self.tm.reset()
            else :
                self.tm.step()

            self.display()
            user_input = self.screen.get_wch()





    def display(self) :
        self.screen.erase()

        # instructions
        self.screen.addstr(0,0, "Any key to step (hold to play)")
        self.screen.addstr(1,0, "'r' to reset")
        self.screen.addstr(2,0, "'q' to quit")

        # information about the machine
        self.screen.addstr(self.tapeH-3,0, 'Step  : ' + str(self.tm.steps))
        self.screen.addstr(self.tapeH-2,0, 'State : ' + str(self.tm.state))
        self.screen.addstr(self.tapeH-4, 0, 'Program : ' + self.tm.path)

        # drawings
        self.screen.hline(self.tapeH-1, 0, curses.ACS_HLINE, self.screenW)
        self.screen.hline(self.tapeH+1, 0, curses.ACS_HLINE, self.screenW)
        self.screen.addch(self.tapeH-3, self.screenW//2, '|')
        self.screen.addch(self.tapeH-2, self.screenW//2, '|')
        self.screen.addch(self.tapeH-1, self.screenW//2, 'V')

        # tape
        left_most_cell = self.tm.pos - self.screenW//2
        right_most_cell = left_most_cell + self.screenW

        for i,cell in enumerate(range(left_most_cell, right_most_cell)) :
            if str(cell) in self.tm.tape.keys() :
                self.screen.addch(self.tapeH, i, self.tm.tape[str(cell)])
