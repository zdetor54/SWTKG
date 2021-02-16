from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, FOAF, XSD

# Part 1
def parseXml2Turtle(file):
    g = Graph()
    g.parse(source=file, format="xml")
    print(g.serialize(format="turtle").decode("utf-8"))
    g.serialize("exc_2.ttl",format="turtle")

parseXml2Turtle("zac_foaf.rdf")

# # Part 2

# def parseTurtle(file):
#     g = Graph()
#     g.parse(source=file, format="ttl")
#     # g.serialize("exc_2.ttl",format="turtle")
#     print(g.serialize(format="turtle").decode("utf-8"))

# parseTurtle("exc_3.ttl")