from wga import diff_level, get_pid, word_maker 

from wgb import obfuscated_view, letter_checker, ascii_draw

print('for quitting, type "quit" command. "new" for starting with new word.')

#################### set dL - difficulty level
dL = diff_level(3) # default Difficulty level

def main_loop():
    wg = [ # wg - word game
    get_pid()        # [0] int pid - process id
    , word_maker(dL) # [1] string - current word
    , 7              # [2] int - lives left
    , dL             # [3] int - difficulty Level
    , set()          # [4] set - letters offered
    , 0              # [5] int - inner loop counter
    ]
    
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
        
        wg[4].add(leIn) ## add offered letter to the set()        
        print(ascii_draw(wg[2]) + str(wg[2]) + " lives left")
        print(letter_checker(wg, leIn))
        print('\t\t\t\t', wg) ## for debugging comment for real game
        print('\n') # just extra line, for visual clarity

main_loop() # starts the main loop