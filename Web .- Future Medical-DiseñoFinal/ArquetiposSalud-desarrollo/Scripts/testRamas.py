import xml.etree.ElementTree as ET

tree = ET.parse('openEHR-EHR-EVALUATION.contraceptive_summary.v0.xml')
root = tree.getroot()
codigos = []
textos = []
atributosx = []

for child1 in root:
    for term in child1.findall('{http://schemas.openehr.org/v1}term_definitions'):
            if term.get('language') == 'en':
                    for items in term.findall('{http://schemas.openehr.org/v1}items'):
                        codigo =  items.get('code')
                        codigos.append(codigo)
                    for child3 in term:
                        for items2 in child3.findall('{http://schemas.openehr.org/v1}items'):
                            if items2.get('id') == 'text': textos.append(items2.text)  
                    break


for i in range (len(codigos)):
    print codigos[i],textos[i]

test = []
finalNodes = []
nodes = []

def buscaNodos(atributoActual, tempNodes,finalNodes):
    tempNodes = []
    for hijo in atributoActual:
        for nodos in hijo:
            if nodos.tag==('{http://schemas.openehr.org/v1}node_id'):
                if str(nodos.text) in codigos:
                        tempNodes.append(nodos.text)
                
    if len(tempNodes)>0:
        finalNodes.append(tempNodes)
    for atributoActual in hijo.iter('{http://schemas.openehr.org/v1}attributes'):
                buscaNodos(atributoActual,tempNodes,finalNodes)
    return finalNodes

for child1 in root:
        for atributos in child1.findall('{http://schemas.openehr.org/v1}attributes'):
            atributosx.append(atributos)

print len(atributosx)
finalNodes.append( buscaNodos(atributosx[0],nodes,finalNodes) )

print finalNodes

input()