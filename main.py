import re

def Add(string):
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
        tempList = []
        negativeError = []
        for i in number_list:
            try:
                temp = int(i)
            except:
                raise TypeError('Cannot be Other than integer')
            if temp < 0 :
                try:
                    raise ValueError('negatives not allowed')
                except ValueError:
                    negativeError.append(str(temp))
                    continue
            tempList.append(temp)
        stringOfNegatives = ','.join(negativeError)
        if len(stringOfNegatives):
            raise ValueError(stringOfNegatives,'negatives are not allowed')
            
        return sum(tempList)
    
    

    
        