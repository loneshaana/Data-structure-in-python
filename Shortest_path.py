def find_shortest(graph,start,end,path=[]):
    paths=[]
    path = path+[start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
    return shortest


graph={'A':['B','C'],'B':['E','D'],'C':['D','F'],'E':['F']}

print find_shortest(graph,'A','F')
