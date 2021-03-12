from rdflib import Graph
import owlrl

g = Graph()
g.parse("lab3_data_graph-full.ttl", format="ttl")
print("Loaded '" + str(len(g)) + "' triples.")


qres = g.query(
"""
SELECT ?countryName (count(?cityName) as ?cityCount) 
WHERE{
    ?country a ex:Country;
            ex:name ?countryName.
    ?city ex:hasCountry ?country;
            ex:name ?cityName.
}
GROUP BY ?countryName
ORDER BY DESC(?cityCount)
""")

#Single row with one boolean vale
for row in qres:
    print(f"{str(row.countryName)},", int(row.cityCount))
