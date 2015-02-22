import getDao as g
from gi.repository import GdkPixbuf, GObject
import threading

class Busqueda(threading.Thread):

  def __init__(self,ventana):
    self.ventana=ventana

  def searchQuotes(self,company,tipo,startDate,endDate):
    #findInstantQuoteByCompany(self,company,startDate,endDate)
    quotes=g.DaoUtil().findInstantQuoteByCompany(company,startDate,endDate)
    lista = []
    for e in quotes:
      lista.append([e.getValue()])
    GObject.idle_add(self.ventana.cargarEnContenedor,self.ventana.window,lista)
