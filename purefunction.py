# a pure function is a function that does not alter variables of the global scope and only perform a small task required of it
# Traditional functions have access to global variables and can alter them. 
string ="reversal"
def string_reversal(str):
    if len(str)==0:
        return str
    else:
        print(string_reversal(str[1:]))
        return string_reversal(str[1:])+str[0]
            
reversed=string_reversal(string)
