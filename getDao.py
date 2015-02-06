import couchdb
import model.couchDB
import config as c
from model.quotes import InstantQuote
import json

class GetDao():

  def __init__(self):
    server = couchdb.Server(c.serverDir)
    bd = server[c.dataBase]
    self.dao=model.couchDB.CouchDBDAO(bd)

  def getDao(self):
    return self.dao

class DaoUtil():

  def __init__(self):
    self.dao = GetDao().getDao()
  #delegacion de los casos de uso, inserciones, busquedas .... , los casos de uso van en otra clase 

  def insert(self,date,company,value):
    #TODO validar date,company y value  y valor de retorno
    quote=InstantQuote(date,company,value)
    self.dao.insert(quote.toDict())

  def findInstantQuoteByCompany(self,company,startDate,endDate):
    self.dao.findInstantQuoteByCompany(company,startDate,endDate)
