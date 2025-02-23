def obfuscated_view(word, setIn):
    oOut = ''
    for l in word:
        if l in setIn:
            oOut += l + ' '
        else:
            oOut += '_ '
    return oOut

def letter_checker(wg, letter):
    if letter in wg[1]:
        lcOut = 'Good, ' + letter + ' is in word'
    elif letter in wg[4]:
        lcOut = 'Letter ' + letter + ' was guessed already before'
    else: 
        lcOut = 'Bad, ' + letter + ' is NOT in word'
        wg[2] -= 1 
        print(ascii_draw(wg[2]) + str(wg[2]) + " lives left\n")      
    return '\n\t' + lcOut

def ascii_draw(drNum):
    # drNum - drawing number
    ad = {} # ascii drawings
    ad[0] = """
    |============
    |          |
    |          o 
    |         | |
    |         / |_
    |=================   """

    ad[1] = """
    |============
    |          |
    |          o 
    |         | |
    |        
    |=================   """

    ad[2] = """
    |============
    |          |
    |          o 
    |        
    |        
    |=================   """

    ad[3] = """
    |============
    |          |
    |         
    |       
    |         
    |=================   """

    ad[4] = """
    |============
    |       
    |         
    |        
    |        
    |=================   """

    ad[5] = """
    |
    |        
    |         
    |        
    |        
    |=================   """

    ad[6] = """
    
    
    
    |
    |
    |=================   """

    ad[7] = """
    
    
    
    
    
    |=================   """

    return ad[drNum]