from enum import Enum

class ColorEnum(str, Enum):
    black= "\033[30m"
    red= "\033[31m"
    green= "\033[32m"
    yellow= "\033[33m"
    blue= "\033[34m"
    magenta= "\033[35m"
    cyan= "\033[36m"
    white= "\033[37m"
    reset = "\033[0m"

class ChalkInstance:
    def __init__(self, color: str, value, withResetAtEnd = True):
        self.__value = "".join([color, str(value)])
        if withResetAtEnd:
            self.reset()
        
    def reset(self):
        self.__value = self.__value + ColorEnum.reset
    
    def __str__(self):
        return self.__value
    
class __Chalk:
    def green(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.green, value, withResetAtEnd)
    
    def red(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.red, value, withResetAtEnd)
    
    def yellow(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.yellow, value, withResetAtEnd)
    
    def blue(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.blue, value, withResetAtEnd)
    
    def magenta(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.magenta, value, withResetAtEnd)
    
    def cyan(self, value, withResetAtEnd = True):
        return ChalkInstance(ColorEnum.cyan, value, withResetAtEnd)
    
    def reset(self) -> str:
        return str(ColorEnum.reset)


chalk = __Chalk()
    