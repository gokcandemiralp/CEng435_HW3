import sys
import socket
INF = sys.maxsize
HOST = "127.0.0.1"

class Edge:
    toNode = None
    cost = INF

    def printEdge(self):
        print(f" -{self.toNode} | {self.cost}")

class Node:
    nodeId = None
    edgesList = []

    def __init__(self,nodeId):
        self.nodeId = nodeId
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST,nodeId))
        self.s.listen()
        self.s.settimeout(5) 

    def updateEdge(self,u_nodeId,u_cost):
        for edge in self.edgesList:
            if(edge.toNode == u_nodeId):
                edge.cost = u_cost

    def printNode(self):
        for edge in self.edgesList:
            print(f"{self.nodeId}", end='')
            edge.printEdge()



read_nodeId = sys.argv[1]
fd = open(f"{sys.argv[1]}.costs", "r")
lineCount = 0
nodeCount = 0

tempNode = Node(int(read_nodeId))

lines = fd.readlines()
for line in lines:
    if(lineCount == 0):
        nodeCount = int(line)
        for i in range(nodeCount):
            tempEdge = Edge()
            tempEdge.toNode = 3000+i
            if(3000+i == tempNode.nodeId):
                tempEdge.cost = 0
            tempNode.edgesList.append(tempEdge)
    else:
        lineElements = line.split(' ')
        tempEdge = Edge()
        destination = int(lineElements[0])
        distance = int(lineElements[1])
        tempNode.updateEdge(destination,distance)

        edge_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            edge_s.connect((HOST, destination))
        except ConnectionRefusedError:
            continue 
    lineCount += 1


tempNode.printNode()