import getDao as g
from gi.repository import GdkPixbuf, GObject
import threading,time
cargado = False
class Busqueda(threading.Thread):

  def __init__(self,ventana):
    self.ventana=ventana

  def searchQuotes(self,company,tipo,startDate,endDate):
    #findInstantQuoteByCompany(self,company,startDate,endDate)
    GObject.idle_add(self.ventana.on_cargando,self.ventana.window)
    horaI="08:00"
    horaF="18:00"
    fInicio=""
    fFin=""
    if tipo=="Hoy":
      tiempo=time.strftime("%d/%m/%Y-", time.gmtime(time.time()))
      fInicio=tiempo+horaI
      fFin=tiempo+horaF
    startDate,endDate=fInicio,fFin
    GObject.idle_add(self.ventana.actualizaLabel,self.ventana.frameCentralLabel,"viendo cotizaciones de "+company+"  "+tipo)
    t1=time.time()
    quotes=g.DaoUtil().findInstantQuoteByCompany(company,startDate,endDate)
    t2=time.time()
    print "Query time :"+str(t2-t1)+" sec"
    lista = []
    for e in quotes:
      lista.append([e.getValue()])
    GObject.idle_add(self.ventana.cargarEnContenedor,self.ventana.window,lista)
    global cargado	
    cargado=True

  def progressBar(self):
    global cargado
    while not cargado:
      GObject.idle_add(self.ventana.on_cargaFinalizada,self.ventana.window)
      time.sleep(0.125)
    cargado=False

