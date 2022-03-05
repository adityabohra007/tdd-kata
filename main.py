

import re
import types


def string_calculator(string):
    if string is None:
        raise TypeError('Cannot be None')
    if not isinstance(string,str):
       raise TypeError('Not a string') 
    
    
    if len(string)==0:
        return 0
    else:
        delimiter = r'[\s,\n]'
        if string.startswith('//'):
            string = string.strip('//');
            delimiter = r'['+string[0]+']'
            string = string.strip(delimiter+'\n')            
            
        if string.endswith('\n'):
            raise SyntaxError('Cannot have newline character at the end of string')
            return
        number_list = re.split(delimiter,string)
        number_list =[int(i) for i in number_list]
        return sum(number_list)
    
    

    
        