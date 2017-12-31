
def find_path(graph,start,end,path=[]):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	if end in graph[start]:
		path = path + [end]
		return path
	else:
		for node in graph[start]:
			if node not in path:
				newpath = find_path(graph,node,end,path)
				if newpath:
					return newpath
		return None


#----------Driver Code---------
graph={'A':['B','C'],'B':['E','D'],'C':['D','F'],'E':['F']}

print find_path(graph,'A','D')
