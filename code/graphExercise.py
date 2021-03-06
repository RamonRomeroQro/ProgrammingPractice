
from collections import deque

def auxb(node, marked):
    queue = deque([])
    marked.append(node)
    queue.append(node)
    while len(queue)>0:
        r=queue.popleft()
        print(r)
        for i in r.nodes:
            if i not in marked:
                marked.append(i)
                queue.append(i)

def breadth(node):
    marked=[]
    auxb(node, marked)


def auxa(node, visited):
    if node == None:
        return 0
    print (node.value)
    visited.append(node)
    for i in node.nodes:
        if i not in visited:
            return auxsearch(i,visited)

def depth(node):
    v=[]
    return auxa(node,v)


class Node(object):
    def __init__(self, id=None, nodes=None):
        self.id = id
        self.nodes=nodes


if __name__ == '__main__':
    a=Node('a')
    b=Node('b')
    c=Node('c')
    d=Node('d')
    e=Node('e')
    f=Node('f')
    g=Node('g')
    h=Node('h')
    i=Node('i')
    j=Node('j')
    a.nodes=[b,c]
    b.nodes=[e,d]
    d.nodes=[f]
    c.nodes=[g,h,i]
    g.nodes=[j]
    h.nodes=[j]
    i.nodes=[j]

    breadth(a)
    depth(a)
