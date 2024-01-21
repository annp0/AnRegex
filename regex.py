from error import *
from syntax import *
from nfa import *
    
class regex:
    def __init__(self, exp : str):
        self.exp = exp
        if (not isValidStr(exp)):
            print("regex("+exp+"): illegal character")
            self.legal = 0
        elif (not isClosed(exp)):
            print("regex("+exp+"): unclosed parenthesis")
            self.legal = 0
        else:
            self.legal = 1
        self.nfa = None
        if self.legal:
            self.legal = self.__compile()
            if not self.legal:
                print("regex("+exp+"): illegal syntax")
        
    
    def __compile(self) -> bool:
        parts = helpPar(0, len(self.exp) - 1, self.exp)
        try:    
            ast1 = helpBar(parts)
            ast2 = helpStar(ast1)
        except SyntaxError:
            return False
        self.nfa = buildNfa(ast2)
        return True

    def match(self, text: str) -> bool:
        if not self.legal:
            print("regex("+self.exp+"): refuse to match ("+text+")")
            return False
        queue = [(0, self.nfa.entry)]
        visited = [(0, self.nfa.entry)]
        while(len(queue) > 0):
            index, state = queue.pop(0)
            if index == len(text):
                if state in self.nfa.exit:
                    return True
                else: continue
            for id, outstate in state.out:
                if id == ' ':
                    can = (index, outstate)
                    if can not in visited:
                        queue.append((index, outstate))
                        visited.append((index, outstate))
                elif isChar(id):
                    if text[index] == id or id == '.':
                        can = (index + 1, outstate)
                        if can not in visited:
                            queue.append((index + 1, outstate))
                            visited.append((index + 1, outstate))
        return False
