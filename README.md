# **cursesTM**

#### *Turing Machine simulation with ncurses gui*
A ncurses application written in python to simulate a turing machine.


![Screenshot of the app after 154 steps of the prog2.txt program](/ScreenShots/prog_screenshot.png)
Screenshot of the app after 154 steps of the prog2.txt program.

## **Known Problems**
- Not tested on Windows yet.

## **Planed features**
- Error checking in program befor running it.
- Travel on the tape to display cells further from the head.


## Dependencies
Python3

## Usage
To install, download this github repository and get inside it :  
`git clone https://github.com/kalharko/cursesTuringMachine`  
`cd cursesTuringMachine`

To use, run the python file called `ctm.py` from inside the cursesTuringMachine folder:  
 `python ctm.py <program file path>`  
 ex : `python ctm.py Examples/prog2.txt`

 To update, simply pull from the github repository :  
 `git pull`  

## Commands

- `q` to quit the app.
- `r` to reset the program.
- Any other key to step the machine. (Hold to play faster)


## **Writting a Program**
You can take inspiration from the Example folder.

### Program information

`input : B` defines the input of the machine, what is written on the tape when the program starts. `B` means blank.  

`start-state : <start state name>` defines the starting state of the machine.  

### State definition

```
<state name>:
<symbol read> | <actions> | <next state name>
<symbol read> | <actions> | <next state name>
```

The actions available in a turring machine are :
- `p<symbol>` to print the symbol to the tape at the current position.
- `e` to erase from the tape at the current position.
- `r` to go right on the tape.
- `l` to go left on the tape.

Example :  
```
Loop:
B | p0r | Loop
```

The state `Loop` will print the symbol `0` and go to the right when encounters a blank cell. The next state being it self, the machine stays in the `Loop` state.
