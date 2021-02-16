'''
Created on 02 Feb 2021

@author: ejimenez-ruiz
'''
from rdflib import Graph

def queryLocalGraph():

    #Example from  https://www.stardog.com/tutorials/data-model/
   
    g = Graph()
    g.parse("playground.ttl", format="ttl")
    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
        
    print("Females:")
    
    qres = g.query(
    """SELECT ?thing ?name where {
      ?thing tto:sex "female" .
      ?thing dbp:name ?name .
    }""")

    for row in qres:
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        print("%s is female with name '%s'" % (str(row.thing),str(row.name)))
        
        
queryLocalGraph()