import xml.etree.ElementTree as ET
import os
import re


def ObtenerDatos(archivos,arch):
    tree = ET.parse(archivos)
    root = tree.getroot()
    codigos = []
    textos = []
    temp = []

    for child1 in root:
        for term in child1.findall('{http://schemas.openehr.org/v1}term_definitions'):
                if term.get('language') == 'en':
                        for items in term.findall('{http://schemas.openehr.org/v1}items'):
                            codigo =  items.get('code')
                            codigos.append(codigo)
                        for child3 in term:
                            for items2 in child3.findall('{http://schemas.openehr.org/v1}items'):
                                if items2.get('id') == 'text':
                                        temp.append(items2.text)
                                if items2.get('id') == 'description':
                                        temp.append(items2.text)
                                        textos.append(temp)
                                        temp = []
                                            
                        break

    
    for i in range (len(codigos)):
        if(codigos[i]!= None and textos[i][0]!=None and textos[i][1]!=None ):
            textos[i][1] = textos[i][1].replace('"','')
            textos[i][1] = re.sub('\s+', ' ', textos[i][1]).strip()

            if i==len(codigos)-1:
                cad = '\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"}\n'
                arch.write(cad)
                arch.write('\t\t]}\n')
            else:
                cad = '\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"},\n'
                arch.write(cad)
  
def Main():
    
    os.chdir("../temp")
    data = os.listdir(".")
    open("../Archivos JSON/test.json", 'w').close()
    arch = open("../Archivos JSON/test.json","w")
    
    for archivo in data:
        tree = ET.parse(archivo)
        root = tree.getroot()
        
        for definition in root.find('{http://schemas.openehr.org/v1}definition'):
            nombre_arquetipo = definition.text
            break      

        arch.write('{"meta":{\n\t"name":"xdd",\n\t"author":"xd",\n\t"version":"xd"},\n\t"format":"node_tree",\n\t"data":{"id":"root","topic":"'+str("Arquetipo")+'","children":[\n\t')

        print "Obteniendo Informacion de ",archivo
        arch.write('\t{"id":"'+str(nombre_arquetipo)+'","topic":"'+str(nombre_arquetipo)+'","expanded":true,"children":[\n')
        ObtenerDatos(archivo,arch)  

    arch.write("\t]}\n}")
Main()

arch = open("../Archivos JSON/test.json")
x = arch.read()
c=0
temp = ""

for i in range(len(x)):
        try:
            if x[i]=="," and x[i+6]=="]" and x[i+7]=="}":
                c+=1
            else:
                temp = temp + str(x[i])
               
        except:
            c+=1

arch = open("../Archivos JSON/test.json",'w')
for i in temp:
    arch.write(i)
arch.close()


