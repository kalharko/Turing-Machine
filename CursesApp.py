import os
from unicurses import *
from TM import TM


class CursesApp() :
    def __init__(self, stdscr, tm):
        self.tm = tm

        # constants
        self.ESCAPE = [CCHAR('q')]

        self.screen = stdscr
        self.screenH, self.screenW = getmaxyx(self.screen)
        self.tapeH = self.screenH//2 + 1
        wrefresh(self.screen)

        init_pair(1, 0,255)

        # Main loop
        self.mainLoop()

        # Exit
        werase(self.screen)
        refresh()



    def mainLoop(self) :
        self.display()
        user_input = getch()

        while not user_input in self.ESCAPE :
            if user_input == 'r' :
                self.tm.reset()
            else :
                self.tm.step()

            self.display()
            user_input = getch()





    def display(self) :
        werase(self.screen)

        # instructions
        mvwaddstr(self.screen, 0,0, "Any key to step (hold to play)")
        mvwaddstr(self.screen, 1,0, "'r' to reset")
        mvwaddstr(self.screen, 2,0, "'q' to quit")

        # information about the machine
        mvwaddstr(self.screen, self.tapeH-3,0, 'Step  : ' + str(self.tm.steps))
        mvwaddstr(self.screen, self.tapeH-2,0, 'State : ' + str(self.tm.state))
        mvwaddstr(self.screen, self.tapeH-4, 0, 'Program : ' + self.tm.path)

        # drawings
        mvwhline(self.screen, self.tapeH-1, 0, ACS_HLINE, self.screenW)
        mvwhline(self.screen, self.tapeH+1, 0, ACS_HLINE, self.screenW)
        mvwaddch(self.screen, self.tapeH-3, self.screenW//2, '|')
        mvwaddch(self.screen, self.tapeH-2, self.screenW//2, '|')
        mvwaddch(self.screen, self.tapeH-1, self.screenW//2, 'V')

        # tape
        left_most_cell = self.tm.pos - self.screenW//2
        right_most_cell = left_most_cell + self.screenW

        for i,cell in enumerate(range(left_most_cell, right_most_cell)) :
            if str(cell) in self.tm.tape.keys() :
                mvwaddch(self.screen, self.tapeH, i, self.tm.tape[str(cell)])

        # machine states description
        height = max([len(x) for x in self.tm.description]) + 1
        x = 0
        for state in self.tm.description :
            for i,line in enumerate(state) :
                mvwaddstr(self.screen, self.screenH-height+i, x, line)
            x += max([len(line) for line in state]) + 5


        wrefresh(self.screen)
