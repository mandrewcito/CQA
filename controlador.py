import getDao as g
from gi.repository import GdkPixbuf, GObject
import threading

class Busqueda(threading.Thread):

  def __init__(self,ventana):
    self.ventana=ventana

  def searchQuotes(self,company,tipo):
    quotes=g.DaoUtil().findByCompany("InstantQuote",company)
    lista = []
    for e in quotes:
      lista.append([e.getValue()])
    GObject.idle_add(self.ventana.cargarEnContenedor,self.ventana.window,lista)
