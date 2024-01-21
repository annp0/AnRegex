'''
Group the Syntax Parts to ASTs
The format of AST: (`symbol, args)
Priority (from high to low):
1. Parenthesis, 2. Union, 3. Repetition 4. Concatenation
'''
def helpPar(start: int, end: int, text : str) -> list:
            index = start
            depth = 0
            result = []
            while(index <= end):
                if text[index] == '(':
                    index = index + 1
                    substart = index
                    while(depth != 0 or text[index] !=')'):
                        if text[index] == '(': depth = depth + 1
                        elif text[index] == ')': depth = depth - 1
                        index = index + 1
                    result.append(helpPar(substart, index - 1, text))
                    index = index + 1
                elif text[index] in ['|', '*']:
                    result.append(text[index])
                    index = index + 1
                else:
                    temp = ''
                    while(index <= end and text[index] not in ['|', '*', '(', ')']):
                        temp = temp + text[index]
                        index = index + 1
                    result.append(temp)
            return result

def helpBar(parts: list):
    global syntaxerror
    index = 0
    while(index < len(parts)):
        if type(parts[index]) is list:
            parts[index] = helpBar(parts[index])
        elif parts[index] == '|':
            if index == len(parts) - 1 or index == 0:
                raise SyntaxError
            return [('|', parts[0:index], helpBar(parts[index+1:]))]
        index = index + 1
    return parts

def helpStar(parts: list):
    global syntaxerror
    index = 0
    while(index < len(parts)):
        if type(parts[index]) is list:
            parts[index] = helpStar(parts[index])
        elif type(parts[index]) is tuple:
            parts[index] = (parts[index][0], helpStar(parts[index][1]), helpStar(parts[index][2]))
        elif parts[index] == '*':
            if index == 0:
                raise SyntaxError
            if type(parts[index - 1]) == str:
                l = len(parts[index - 1])
                parts[index] = ('*', [parts[index-1][-1]])
                parts[index-1] = parts[index-1][0:(l-1)]
            else:
                parts[index] = ('*', parts[index-1])
                parts[index-1] = ''
        index = index + 1
    return [x for x in parts if x != '']