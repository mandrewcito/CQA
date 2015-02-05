#/usr/bin/env python
# --*-- coding: utf-8 --*--
import model.getData.getIbex as getIbex
import getDao as g
import time
import UTIL.dateUtil as dt
import config

def estaActualizado(fechaActualizacion):
  return dt.esMasReciente(fechaActualizacion,config.lastUpdate)

def insertar(dao,date,(company,value)):
  dao.insert(date,company,value)

def main():
  lista_valores,fechaActualizacion=getIbex.main()
  if not estaActualizado(fechaActualizacion):
    print "los valores no han sido actualizados"
    return -1
  #else actualizar fecha!
  dao=g.DaoUtil()
  for valor in lista_valores :
    insertar(dao,date,valor)

if __name__ == "__main__":
  main()
