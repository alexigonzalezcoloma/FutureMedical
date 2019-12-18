
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
            if estado=='Final':
                if i==len(codigos)-1:
                    cad = '{"titulo":"'+str(textos[i][0].encode('utf-8').strip())+'", \n"descripcion":"'+str(textos[i][1].encode('utf-8').strip())+'"}\n'
                    arch.write(cad)
                else:
                    cad = '{"titulo":"'+str(textos[i][0].encode('utf-8').strip())+'", \n"descripcion":"'+str(textos[i][1].encode('utf-8').strip())+'"},\n'
                    arch.write(cad)
            else:
                cad = '{"titulo":"'+str(textos[i][0].encode('utf-8').strip())+'", \n"descripcion":"'+str(textos[i][1].encode('utf-8').strip())+'"},\n'
                arch.write(cad)
            #print codigos[i],textos[i]
  


def Main():
    os.chdir("entry")
    data = os.listdir(".")
    estado = 'notFinal'
    arch = open("../arquetipesx.json","a")
    arch.write('{\n"arquetipos":[\n')
    for carpetas in data:
        os.chdir(carpetas)
        data2 = os.listdir(".")
        print "############ Carpeta: ",carpetas," ############"
        for archivos in data2:
            if data.index(carpetas)==len(data)-1:
                if data2.index(archivos) == len(data2)-1:
                    estado = 'Final'
                    print "Obteniendo Informacion de ",archivos
                    ObtenerDatos(archivos,arch,estado)
                    print "\n"
                else:
                    print "Obteniendo Informacion de ",archivos
                    ObtenerDatos(archivos,arch,estado)
                    print "\n"  
            else:
                print "Obteniendo Informacion de ",archivos
                ObtenerDatos(archivos,arch,estado)
                print "\n"  
        os.chdir("..")
    arch.write("]}")
Main()
