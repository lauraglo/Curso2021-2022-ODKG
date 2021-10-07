# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tV5j-DRcpPtoJGoMj8v2DSqR_9wyXeiE

**Task 07: Querying RDF(s)**
"""


from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS
from rdflib import Graph, Namespace, Literal

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind(
    'vcard',
    Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"),
    override=False
)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

ns = Namespace("http://somewhere#")


"""
**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

"""
print("========================= 7.1 ============================")

# RDFLib
for s, p, v in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

print("-----------------------------------------------------------")
subclassesOfPerson = g.query(prepareQuery(
    '''
        SELECT DISTINCT ?sc WHERE { 
            ?sc rdfs:subClassOf  ns:Person. 
        } 
    ''',
    initNs={"rdfs": RDFS, "ns": ns}
))

# SPARQL
for sub in subclassesOfPerson:
    print(sub)


"""
**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
"""


print("========================= 7.2 ============================")

# RDFLib
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for ss, sp, so in g.triples((None, RDF.type, s)):
        print(ss)

print("-----------------------------------------------------------")
# SPARQL
people = g.query(prepareQuery(
    '''
        SELECT ?person WHERE { 
            ?sub rdfs:subClassOf* ns:Person.
            ?person a ?sub
        }
    ''',
    initNs={"ns": ns, "rdf": RDF})
)

for person in people:
    print(person)


"""
**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""

print("========================= 7.3 ============================")

# RDFLib
for s, p, o in g.triples((None, RDF.type, ns.Person)):  # Individuals of Person (P)
    for sP, pP, oP in g.triples((s, None, None)):
        print(sP, pP, oP)
# Individuals of one of the subclasses of Person (SC)
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for sSC, pSC, oSC in g.triples((None, RDF.type, s)):
        for sSCP, pSCP, oSCP in g.triples((sSC, None, None)):
            print(sSCP, pSCP, oSCP)


print("------------------------------------------")

# SPARQL
people = g.query(prepareQuery(
    '''
        SELECT ?s ?p ?v
        WHERE { 
            ?s_ rdfs:subClassOf* ns:Person.
            ?s a ?s_.
            ?s ?p ?v
        }
    ''',
    initNs={"ns": ns, "rdf": RDF})
)

for person in people:
    print(person)