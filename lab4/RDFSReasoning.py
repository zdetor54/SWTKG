
from rdflib import Graph

import owlrl


def RDFSInference():
    
    g = Graph()
    
    g.parse("lab4.ttl", format="ttl")    
    
    print("Loaded '" + str(len(g)) + "' triples.")
    
    #Performs RDFS reasoning
    owlrl.DeductiveClosure(owlrl.RDFS_Semantics, axiomatic_triples=True, datatype_axioms=False).expand(g)
    
    
    print("After inference rules: '" + str(len(g)) + "' triples.")
    
    print("Saving extended graph'")
    g.serialize(destination='lab4_inference.ttl', format='ttl')
    
def queryLocalGraph(file):
    g = Graph()
    g.parse(file,format="ttl")
    print(f"file: {file} has been loaded")
    # print(g.serialize(format="turtle").decode("utf-8"))

    qres = g.query(
    """ask {:Ann a :Child .}""")


    for row in qres:
        #Row is a list of matched RDF terms: URIs, literals or blank nodes
        print(f"{(str(row))}")




queryLocalGraph("lab4_inference.ttl")
# RDFSInference()