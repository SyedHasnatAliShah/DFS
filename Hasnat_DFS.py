#Syed Hasnat Ali Shah (01-131162-029)
import time
from collections import defaultdict,deque 
class Graph:
    def __init__(self):
        self.list_neighbor = defaultdict(list)
        self.list_node =defaultdict(list)
    def add_node(self,node):
        self.list_node[node] = True

    def add_edge(self,node,nodebis):
        try :
            self.list_neighbor[node].append(nodebis)
        except :
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)
        try :
            self.list_neighbor[nodebis].append(node)
        except :
            self.list_neighbor[nodebis] = []
            self.list_neighbor[nodebis].append(node)
    def neighbors(self,node):
        try :
            return self.list_neighbor[node]
        except :
            return []
    def nodes(self):
        return self.list_node.keys()
    def delete_edge(self,node,nodebis):
        self.list_neighbor[node].remove(nodebis)
        self.list_neighbor[nodebis].remove(node)
    def delete_node(self,node):
        del self.list_node[node]
        try :
            for nodebis in self.list_neighbor[node] :
                self.list_neighbor[nodebis].remove(node)
            del self.list_neighbor[node]
        except :
            return "error"
        #s==startNode, f==finalNode
    def dfs(self, s,f):
        start = time.time()
        visited = set()
        stack = [s]
        while stack:
            s = stack.pop()
            if s==f:
                print("",f)
                break
            if s not in visited:
                print(s, end=" ")
                visited.add(s)
                stack.extend(self.list_neighbor[s])
        end = time.time()
        
        print("Execution time:-")
        print(end - start," SECONDS")
if __name__ == "__main__":
    G = Graph()
    totalNode=int(input("Enter Total num of node:"))
    for node in range(totalNode):
        eachNode=int(input("Enter node: "))
        G.add_node(eachNode)

    totalEdges=int(input("Enter Total num of edges:"))
    for node in range(totalEdges):
        startEdge=int(input("Enter 1 Edge node: "))
        endEdge=int(input("Enter 2 Edge node: "))
        print("-"*50)
        G.add_edge(startEdge,endEdge)
    
    initialNode=int(input("Enter starting node:"))
    goalNode=int(input("Enter goal node:"))
    print( G.dfs(initialNode,goalNode))
    
