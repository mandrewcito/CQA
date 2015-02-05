#/usr/bin/env python
# --*-- coding: utf-8 --*--
#Obtiene los datos del ibex-35 y los almacena en una lista de tuplas (empresa,valor) fuerza bruta es caca de la vaca 
import urllib2,sys
import codecs
import time

def parsingTablaValores(tabla):
  lineas=tabla.split("\n")
  lineas=lineas[1:len(lineas)-1]
  lista=[]
  i=0
  while i <len(lineas):
    empresa=lineas[i+1].split("title=\"")[1].split("\">")[0].decode("utf-8", "replace")
    valor=lineas[i+2].split("<td>")[1].split("</td>")[0].replace(",",".")
    lista.append((empresa,valor))
    i+=5
  return lista

def getTablaValores(pag):
  hora =pag.split("<table class=\"m-ranking border n-width mod-ultimos-valores\">")
  tabla=hora[1]
  hora =hora[0].split("<div class=\"values-right\"><time>")[1].split("h</time>")[0]
  tabla=tabla.split("</table>")[0]
  tabla=tabla.split("<tbody xmlns:msxsl=\"urn:schemas-microsoft-com:xslt\" xmlns:vb_user=\"urn:infobolsa\">")[1]
  tabla=tabla.split("</tbody>")[0]
  return tabla,hora
  
def main():
  # Get the total number of args passed 
  total = len(sys.argv)-1
  # Get the arguments list 
  args = sys.argv[1:]
  response = urllib2.urlopen("http://www.finanzas.com/ibex-35/")
  pag=response.read()
  tablaValores,hora=getTablaValores(pag)
  listaIbex=parsingTablaValores(tablaValores)
  date=time.strftime("%d/%m/%Y-", time.gmtime(time.time()))
  date=date+hora
  return listaIbex,date

if __name__ == "__main__":
  main()
