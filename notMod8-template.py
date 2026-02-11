
from universal import universal
import utils
from utils import rf

# Oracle function  -- assume it exists to prove 
# by contradiction that it cannot possibly exist
  
# Assume without loss of generality that altersYesNotMod8 lives in altersYesNotMod8.py
def altersYesNotMod8(inString):
     #** L0210: Add code needed before the call to universal()

    # progString == 1st arg to yesViaNotMod8
    # viaInString == 2nd arg to yesViaNotMod8
    result = universal(progString,viaInString)

     #** L0210: Add code needed after the call to universal()

def yesViaNotMod8(progString,inString):
    #** L0210: Add code needed before call to notMod8()

    #** L0210: Add 2nd arg to notMod8 call, if needed.
    #** If not needed, erase ', . . .'
    val = notMod8(rf(' altersYesNotMod8.py'), . . .)
    
    #** L0210: Add code needed after call to notMod8()

'''
L0210:  Explain why the Python code above proves that notMod8 is undecidable.

L0210:  Expain why you do or do not think that notMod8 is recognizable.
'''
