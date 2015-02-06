#/usr/bin/env python
# --*-- coding: utf-8 --*--
import model.getData.getIbex as getIbex
import getDao as g
import time
import UTIL.dateUtil as dt
import ConfigParser

def setLastUpdate(fecha):
  config = ConfigParser.ConfigParser()
  config.read("config.ini")
  cfgfile = open("config.ini",'w')
  config.set('actualizacion','lastUpdate',fecha)
  config.write(cfgfile)
  cfgfile.close()

def getLastUpdate():
  config = ConfigParser.ConfigParser()
  config.read("config.ini")
  return config.get("actualizacion",'lastUpdate')

def estaActualizado(fechaActualizacion):
  lastUpdate=getLastUpdate()
  print lastUpdate,fechaActualizacion
  return dt.esMasReciente(fechaActualizacion,lastUpdate)

def insertar(dao,date,(company,value)):
  dao.insert(date,company,value)

def main():
  lista_valores,fechaActualizacion=getIbex.main()
  if not estaActualizado(fechaActualizacion):
    print "los valores no han sido actualizados"
    return -1
  else:
    setLastUpdate(fechaActualizacion)
  #else actualizar fecha!
  dao=g.DaoUtil()
  for valor in lista_valores :
    insertar(dao,fechaActualizacion,valor)

if __name__ == "__main__":
  main()
