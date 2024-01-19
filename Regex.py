class Regex:
    def __init__(self, exp : str):
        self.exp = exp
    
    def toParts(self):
        '''
        Parse the Expression to Syntax Parts
        '''
        def helper(start: int, end: int):
            index = start
            depth = 0
            nodes = []
            while(index <= end):
                if self.exp[index] == '(':
                    index = index + 1
                    substart = index
                    while(depth != 0 or self.exp[index] !=')'):
                        if self.exp[index] == '(': depth = depth + 1
                        elif self.exp[index] == ')': depth = depth - 1
                        index = index + 1
                    nodes.append(helper(substart, index - 1))
                elif self.exp[index] == '|':
                    nodes.append('|')
                else:
                    nodes.append(self.exp[index])
                index = index + 1
            return nodes
        return helper(0, len(self.exp) - 1)
    
    def toASTs(self):
        '''
        Group the Syntax Parts to ASTs
        The format of AST: (`symbol, args)
        '''
        def helper(nodes):
            index = 0
            result = []
            altFlag = 0
            while(index < len(nodes)):
                if type(nodes[index]) is list:
                    result.append(helper(nodes[index]))
                elif nodes[index] == '*':
                    a1 = result.pop()
                    result.append(('*', a1))
                elif nodes[index] == '|':
                    altFlag = 1
                    index = index + 1
                    continue
                else:
                    result.append(nodes[index])
                if altFlag:
                    altFlag = 0
                    a1 = result.pop()
                    a2 = result.pop()
                    result.append(('|', a1, a2))
                index = index + 1
            return result
        return helper(self.toParts())

    def AST2NFA(self):
        pass

    def match(text: str):
        pass
            

r = Regex('a|(c*st)*b')
print(r.toParts())
print(r.toASTs())