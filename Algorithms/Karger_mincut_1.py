#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 12:59:46 2020

@author: ElAwbery
"""

"""
The file contains the adjacency list representation of a simple undirected graph. 
There are 200 vertices labeled 1 to 200. The first column in the file represents 
the vertex label, and the particular row (other entries except the first column) 
tells all the vertices that the vertex is adjacent to. So for example, the 6 
th row looks like : "6	155	56	52	120	......". This just means that the vertex 
with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 
155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min 
cut problem and use it on the above graph to compute the min cut. 
(HINT: Note that you'll have to figure out an implementation of edge contractions. 
Initially, you might want to do this naively, creating a new graph from the old 
every time there's an edge contraction. But you should also think about more 
efficient implementations.) 
(WARNING: As per the video lectures, please make sure to run the algorithm many 
times with different random seeds, and remember the smallest cut that you ever 
find.) 
Write your numeric answer in the space provided. So e.g., if your answer is 5, 
just type 5 in the space provided.
"""

import random, re

default_karger_path = '/local/path/to/kargerMinCut.txt'

def make_graph(path):
    '''opens a text file with data in lines and columns
    returns a dict of first_of_line keys and rest_of_line lists as values'''
    # Make a dict of edges from the text file
    # The dict key is a vertex, the values are lists of its adjacent vertices
    edges = {}
    
    data = open(path, 'r')
    lines = data.readlines()
    data.close()

    for line in lines:
        # Different test case files are tab vs space delimited
        regex = re.compile("\s")
        fields = regex.split(line.rstrip())
        edges[fields[0]] = fields[1:]

    return edges

def karger(trials, graph_path = default_karger_path):
    '''Karger's algorithm'''
    
    minimum = float("inf")
    for sim in range(0, trials):
        graph = make_graph(graph_path)
        result = karger_trial(graph)
        minimum = min(result, minimum)
        
    return minimum

def karger_trial(graph):
    '''graph is a dictionary with string keys and list values
    returns the number of cut edges in a randomly chosen cut (not necessarily 
    a min-cut)'''
    
    # Make a list of vertices
    vertices = []
    for key in graph:
        vertices.append(key)
        
    while len(vertices) > 2:
        
        # randomly choose a vertex
        vertex = random.choice(vertices)
        
        # randomly choose another vertex adjacent to vertex
        adj_vertex = random.choice(graph[vertex])
        
        # Add adj_vertex edges to vertex
        for edge in graph[adj_vertex]:
            graph[vertex].append(edge)
        
        # replace all graph instances of adj_vertex with vertex
        graph = replace_all(graph, vertex, adj_vertex)
        
        # Delete the adjacent vertex from graph
        del(graph[adj_vertex])
        
        # Delete adjacent vertex from vertices
        vertices.remove(adj_vertex)
        
        #Remove all self loops from vertex
        graph[vertex] = remove_self_loops(graph, vertex)
    
    cut_edges = len(graph[vertices[0]])
    assert  cut_edges == len(graph[vertices[1]])
        
    return cut_edges


def replace_all(graph, vertex, adj_vertex):
    '''replaces all instances of adj_vertex from a graph's values with vertex'''
    adjacencies = graph[adj_vertex] #correct
    
    # For every connection, change adj_vertex to vertex
    for adjacency in adjacencies:
        # Walk through all the values in case there are parallel paths
        for vertices in graph[adjacency]:
            if vertices == adj_vertex:
                graph[adjacency].remove(adj_vertex)
                graph[adjacency].append(vertex)
    return graph

           
def remove_self_loops(graph, vertex):
    graph[vertex] = [thing for thing in graph[vertex] if thing != vertex]
    return graph[vertex]

  
    
test1 = {
'1': ['2','2','2'],

'2': ['1','1','1'],
    }

karger_trial(test1)

test2 = {
'1': ['2', '3'],

'2': ['1', '3'],

'3': ['1', '2'],
    }

karger_trial(test2)

test3 = {
'1': ['2', '3', '4'],

'2': ['1', '3', '4'],

'3': ['1', '2', '4'],

'4': ['1', '2', '3'],
    }

karger_trial(test3)

test4 = {
'1': ['2', '3', '4', '7'],

'2': ['1', '3', '4'],

'3': ['1', '2', '4'],

'4': ['1', '2', '3', '5'],

'5': ['4', '6', '7', '8'],

'6': ['5', '7', '8'],

'7': ['1', '5', '6', '8'],

'8': ['5', '6', '7'],      
        }

karger_trial(test4)
