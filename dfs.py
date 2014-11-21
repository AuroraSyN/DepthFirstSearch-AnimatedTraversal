#!/usr/bin/env python
import random
import pylab
from matplotlib.pyplot import pause
import networkx as nx
import numpy as np
from pythonds.graphs import Graph, Vertex

pylab.ion()

G = nx.DiGraph()
node_number = 0
node_colors = []
vertices = []
edges = []

node_colors_hash = {}

############################ Draw Graph ########################
def draw_graph(graph, node_size):
    global node_colors, node_colors_hash
    global G
    global vertices, edges
    
    # Turn graph to edge list
    for k,e in graph.iteritems():
        x = [k]*len(e)
        edges.extend(zip(x, e))


    vertices = set([n1 for n1, n2 in edges] + [n2 for n1, n2 in edges])
    node_colors_hash = {x:"white" for x in vertices}
    
    for k,v in node_colors_hash.iteritems():
        node_colors.append(v)
    
    nx.set_edge_attributes(G, 'name', vertices)

    # add nodes
    for node in vertices:
        G.add_node(node)
    
    # add edges
    for edge in edges:
        G.add_edge(edge[0], edge[1], arrows=True)
    
    # set edge colors
    unique_edges = []
    print edges
    for (x, y) in edges:
        if ((y, x) or (y,x)) not in unique_edges:
            unique_edges.append((x,y))

    edge_colors = ["red" for x in unique_edges]

    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels=True,node_size = 600, node_color=node_colors, edge_color=edge_colors)
                               
    # show graph
    pylab.show()
    pause(3)

###################### Depth First Search ######################
def dfs(g):
    for u in g.getVertices():
        if g.getVertex(u).getColor() == 'white':
            print "Start with node: %s" % u
            dfs_visit(g, g.getVertex(u))

def dfs_visit(g, u):
    print "\t Checking node: %s" % u.getId()
    u.setColor('gray')
    change_node_color('gray', u.getId())

    for v in u.getConnections():
        print "From %s trying to go to %s" % (u.getId(), v.getId())
        if v.getColor() == 'white':
     #       v.setPred(u)
            dfs_visit(g, v)
    
    u.setColor('black')
    change_node_color('black', u.getId())

######################### Utility Functions #####################
def change_node_color(c, node):
    global node_colors_hash
    global node_colors
    
    node_colors = []

    # Color the visited node
    node_colors_hash[node]=c

    for k,v in node_colors_hash.iteritems():
        node_colors.append(v)
    
    pos = nx.shell_layout(G)
    nx.draw(G, pos,node_size = 600, node_color = node_colors )
    pylab.draw()
    pause(4)
            

def get_edges(g):
    for u in g.getVertices():
        print "For %s" % u
        for v in g.getVertex(u).getConnections():
            print "\t%s" % v              

############################# Start the Program ##################
# 1. Declare the graph
graph = {1: [2, 4],
        2: [5],
        3: [6, 5],
        4: [2],
        5: [4],
        6: [6] }

# 1. Create graph
graphl = Graph()

for k,v in graph.iteritems():
    graphl.addVertex(k)
    for i in v:
        graphl.addEdge(k, i)

# 2. Draw the graph
draw_graph(graph, len(edges) )

# 3. Run the algorithm
dfs(graphl)
