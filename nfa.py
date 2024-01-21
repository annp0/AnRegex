'''
construction of the nondeterministic finite automata
'''

nodeCount = 0

class node:
    def __init__(self):
        global nodeCount
        nodeCount = nodeCount + 1
        self.id = nodeCount
        self.out = []

class graph:
    def __init__(self, entry: node, exit: list):
        self.entry = entry
        self.exit = exit
    
    def star(self):
        for n in self.exit:
            n.out.append((' ', self.entry))

def concat(g1: graph, g2: graph):
    for n in g1.exit:
        n.out.append((' ', g2.entry))
    return graph(g1.entry, g2.exit)

def bar(g1: graph, g2: graph):
    head = node()
    head.out = [(' ', g1.entry), (' ', g2.entry)]
    return graph(head, g1.exit + g2.exit)

def buildPlain(text: str) -> graph:
    head = node()
    p = head
    for s in text:
        n = node()
        p.out = [(s, n)]
        p = n
    return graph(head, [p])

def buildNfa(ast: list) -> graph:
    index = 0
    prev = None
    while(index < len(ast)):
        if type(ast[index]) == str:
            cur = buildPlain(ast[index])
            prev = concat(prev, cur) if prev != None else cur
        elif type(ast[index]) == list:
            cur = buildNfa(ast[index])
            prev = concat(prev, cur) if prev != None else cur
        elif type(ast[index]) == tuple:
            if ast[index][0] == '*':
                cur = buildNfa(ast[index][1])
                cur.star()
                prev = concat(prev, cur) if prev != None else cur
            elif ast[index][0] == '|':
                cur1 = buildNfa(ast[index][1])
                cur2 = buildNfa(ast[index][2])
                prev = concat(prev, bar(cur1, cur2)) if prev != None else bar(cur1, cur2)
        index = index + 1
    return prev