from wga import diff_level, get_pid, word_maker 

from wgb import obfuscated_view, letter_checker, ascii_draw

print('for quitting, type "quit" command. "new" for starting with new word.')

#################### set dL - difficulty level
dL = diff_level(3) # default Difficulty level
dM = 1 # development Mode 1 - yes, 0 - no, don't show data on screen

def main_loop():
    wg = [ # wg - word game
    get_pid()        # [0] int pid - process id
    , word_maker(dL) # [1] string - current word
    , 7              # [2] int - lives left
    , dL             # [3] int - difficulty Level
    , set()          # [4] set - letters offered
    , 0              # [5] int - inner loop counter
    ]
    
    if dM == 1:
        print('\t\t\t\t', wg, '\n') # on main loop starting state

    
    while True:
        wg[5]+=1
        obf = obfuscated_view(wg[1], wg[4])
        if wg[2] > 0:
            askLetter = str(wg[0]) + " - " + str(wg[5]) + ' For word "' + obf + '" enter a letter: '
        else:
            askLetter = 'Game over, type "new" for new word or "quit" for quitting: '
        leIn = input(askLetter)        
        if leIn == 'quit':
            print('..quitting, good bye')
            break
        if leIn == 'new':
            print('\n')
            main_loop()
            break
                 
        print(letter_checker(wg, leIn))  
        wg[4].add(leIn) ## add offered letter to the set()     
        if dM == 1:
            print('\t\t\t\t', wg, '\n') # dM 1, debugging mode
        else:
            print('\t\t\t\t', wg[4], 'have', wg[2], 'live(s) left', f'(iteration {wg[5]} ended)')
        print('\n') # just extra line, for visual clarity

main_loop() # starts the main loop