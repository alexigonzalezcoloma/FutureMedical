
import xml.etree.ElementTree as ET
import os
import re


def ObtenerDatos(archivos,arch,estado):
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
            if estado=='finCaAr':
                if i==len(codigos)-1:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"}\n'
                    arch.write(cad)
                    arch.write('\t\t\t\t]}\n')
                else:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"},\n'
                    arch.write(cad)
                    
            if estado=='finAr':
                if i==len(codigos)-1:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"}\n'
                    arch.write(cad)
                    arch.write('\t\t\t\t]}\n')
                else:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"},\n'
                    arch.write(cad)
                    
            if (estado=='notFinal'):
                if i==len(codigos)-1:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"}\n'
                    arch.write(cad)
                else:
                    cad = '\t\t\t\t\t{"id":"'+str(codigos[i].encode('utf-8').strip())+'", "topic":"'+str(textos[i][0].encode('utf-8').strip())+'"},\n'
                    arch.write(cad)


             
  
def Main():
    os.chdir("../entry")
    data = os.listdir(".")
    estado = 'notFinal'
    arch = open("../Archivos JSON/arq2.json","w")
    arch.write('{"meta":{\n\t"name":"xd",\n\t"author":"xd",\n\t"version":"xd"},\n\t"format":"node_tree",\n\t"data":{"id":"root","topic":"Arquetipos","children":[\n\t')
    for carpetas in data:
        os.chdir(carpetas)
        data2 = os.listdir(".")
        print "############ Carpeta: ",carpetas," ############"
        arch.write('\t\t{"id":"'+str(carpetas)+'","topic":"'+str(carpetas)+'","expanded":false,"children":[\n')
        for archivos in data2:
            if data.index(carpetas)==len(data)-1:
                if data2.index(archivos) == len(data2)-1:
                    estado = 'finCaAr'
                    print "Obteniendo Informacion de ",archivos
                    arch.write('\t\t\t\t{"id":"'+str(archivos)+'","topic":"'+str(archivos)+'","children":[\n')
                    ObtenerDatos(archivos,arch,estado)
                    print "\n"
                else:
                    estado = 'notFinal'
                    arch.write('\t\t\t\t{"id":"'+str(archivos)+'","topic":"'+str(archivos)+'","children":[\n')
                    ObtenerDatos(archivos,arch,estado)
                    arch.write('\t\t\t\t]},\n')
                    print "\n"  
            else:
                if data2.index(archivos) == len(data2)-1:
                    estado = 'finAr'
                    arch.write('\t\t\t\t{"id":"'+str(archivos)+'","topic":"'+str(archivos)+'","children":[\n')
                    print "Obteniendo Informacion de ",archivos
                    ObtenerDatos(archivos,arch,estado)
                    print "\n"
                else:
                    estado = 'notFinal'
                    arch.write('\t\t\t\t{"id":"'+str(archivos)+'","topic":"'+str(archivos)+'","children":[\n')
                    ObtenerDatos(archivos,arch,estado)
                    arch.write('\t\t\t\t]},\n')

        if data.index(carpetas)==len(data)-1:
            arch.write("\t\t]}\n")    
        else:
            arch.write("\t\t]},\n")
        os.chdir("..")
    arch.write("]}\n}")
Main()

arch = open("../Archivos JSON/arq2.json")
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

arch = open("../Archivos JSON/arq2.json","w")
for i in temp:
    arch.write(i)
arch.close()
