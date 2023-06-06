def shortestPath(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return[]
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = shortestPath(graph,node,end,path)
            if newpath:
                if not shortest or len(newpath)<len(shortest):
                    shortest = newpath
    return shortest

def findAllShortestPath(allpath,shortpath):
    listShortest = []
    for path in allpath:
        if len(path) == len(shortpath):
            listShortest.append(path)
    return listShortest

def allPath(graph,start,end,path=[]):
    path = path +[start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if not node in path:
            newpath = allPath(graph,node,end,path)
            for newpaths in newpath:
                paths.append(newpaths)
    return paths

def findAllEdge(graph):
    ListEdge = []
    for i in graph.keys():
        if graph[i] != []:
            for j in graph[i]:
                temp = i+' => '+j
                ListEdge.append(temp)
    return ListEdge

def printGraph(path):
    for i in range(len(path)):
        print('Path',i+1,'=',path[i])


graphList = {
    'A': ['C','D'],
    'B': ['C','E'],
    'C': ['A','B','D','E'],
    'D': ['C','E'],
    'E': ['C','B'],
    'F': []
}
# edge = findAllEdge(graphList)
# printGraph(edge)
jalur = allPath(graphList,'A','E')
# printGraph(jalur)
shortest = shortestPath(graphList,'A','E')
listshortest = findAllShortestPath(jalur, shortest)
printGraph(listshortest)