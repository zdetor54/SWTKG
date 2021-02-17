from rdflib import Graph
import owlrl

def queryLocalGraph(file, triple):
    g = Graph()
    g.parse(file,format="ttl")

    qres = g.query("""ask""" + triple)
    print(f"Statement: {triple} is {qres.askAnswer}")


questions = [":Father rdfs:subClassOf :Person ."
,":Woman rdfs:subClassOf :Person ."
,":Juliet a :Person ."
,":Ann a :Child ."
,":Ann :isChildOf :Carl ."
,":Ann :hasParent :Juliet ."
,"rdfs:range rdf:type rdfs:Resource ."
,":Mother rdfs:subClassOf :Person ."]

for question in questions:
    queryLocalGraph("lab4_inference.ttl", '{' + question + '}')
