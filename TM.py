import sys

# set this to False if your terminal does not support ANSI color codes
COLORS = True

class TM :
    def __init__(self, path=None) :
        self.tape = {}
        self.pos = 0

        self.states = []
        self.logic = {}
        self.input = ''

        self.steps = 0

        self.description = []

        self.path = path
        if path != None :
            self.open(path)


    def open(self, path) :
        with open(path, 'r') as file :
            for line in file.readlines() :
                line = line.rstrip('\n').rstrip('\r').rstrip(' ')

                # Emplty line or comment
                if line == '' or line [0] == '#' :
                    pass

                # Input
                elif line.split(':')[0].rstrip(' ') == 'input' :
                    self.input = line.split(':')[1].lstrip(' ')

                # Start state
                elif line.split(':')[0].rstrip(' ') == 'start-state' :
                    self.start_state = line.split(':')[1].lstrip(' ')

                # Enter new state definition
                elif line[-1] == ':' :
                    self.states.append(line[:-1])
                    self.description.append([line])

                else :
                    self.description[-1].append(line)
                    # Clean extra spaces
                    line = line.split('|')
                    for i in range(len(line)) :
                        line[i] = line[i].lstrip(' ').rstrip(' ')


                    # Read line info
                    symbol = line[0].split(',')
                    operations = line[1].split(',')
                    final_state = [line[2]]

                    # Register info
                    for s in symbol :
                        self.logic[self.states[-1]+','+s] = operations + final_state

        self.state = self.start_state
        self.pos = 0

        # writes the input on the tape
        self.tape.clear()
        i = 0
        for char in self.input :
            if char == ' ' or char == 'B':
                continue
            else :
                self.tape[str(i)] = char
                i += 1


    def step(self) :
        self.steps += 1

        if str(self.pos) in self.tape.keys() :
            action = self.state + ',' + self.tape[str(self.pos)]
        else :
            action = self.state + ',B'
        action = self.logic[action]

        for step in action[:-1] :
            if step == '' :
                continue

            elif step[0] in ['p', 'P'] :
                self.tape[str(self.pos)] = step[1]  # Print
            elif step[0] in ['e', 'E'] :
                del self.tape[str(self.pos)]     # Erase

            elif step[0] in ['r', 'R'] :       # Right
                self.pos += 1
            elif step[0] in ['l', 'L'] :       # Left
                self.pos -= 1

            else :
                continue

        self.state = action[-1]


    def reset(self) :
        self.open(self.path)


    def __str__(self) :
        out = ''
        for i in range(self.size) :
            fill = ' '
            if i == self.pos:
                if COLORS:
                    fill = '\033[1m>'
                else:
                    fill = '>'
            elif i == self.pos + 1:
                if COLORS:
                    fill = '<\033[0m'
                else:
                    fill = '<'

            if self.tape[i] == None :
                out += fill + ' '
            else :
                out += fill + self.tape[i]

        return out
