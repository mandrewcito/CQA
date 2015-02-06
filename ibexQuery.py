#/usr/bin/env python
# --*-- coding: utf-8 --*--
import model.getData.getIbex as getIbex
import getDao as g
import time
import UTIL.dateUtil as dt
import UTIL.configUtil as cfg

def setLastUpdate(fecha):
  cfg.setTag("config.ini","actualizacion","lastUpdate",fecha)

def getLastUpdate():
  return cfg.getTag("config.ini","actualizacion","lastUpdate")

def estaActualizado(fechaActualizacion):
  lastUpdate=getLastUpdate()
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
  dao=g.DaoUtil()
  for valor in lista_valores :
    insertar(dao,fechaActualizacion,valor)
  return 0

if __name__ == "__main__":
  main()
