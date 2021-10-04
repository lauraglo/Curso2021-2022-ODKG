# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YvqpOFCzor1XBvVX_is8meCSdx7TOGPJ

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

for s,p,o in g:
  print(s,p,o)

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

ns = Namespace("http://somewhere#")
# TO DO
q1 = prepareQuery('''
  SELECT ?Subclass WHERE { 
    ?Subclass rdfs:subClassOf ?Person. 
  }
  ''',
  initNs = { "rdfs": RDFS}  
)
# Visualize the results
for r in g.query(q1, initBindings = {'?Person' : ns.Person}):
 print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery('''
  SELECT ?Subject WHERE {
    ?Class rdfs:subClassOf* ?Person.
    ?Subject rdf:type ?Class
  }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF}  
)
for r in g.query(q2, initBindings = {'?Person' : ns.Person}):
 print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO (We assume that we only want the 'property' itself, not the result)
q3 = prepareQuery('''
  SELECT ?Subject ?Prop WHERE {
    ?Class rdfs:subClassOf* ?Person.
    ?Subject rdf:type ?Class.
    ?Subject ?Prop ?x
  }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF}  
)
for r in g.query(q3, initBindings = {'?Person' : ns.Person}):
 print(r)