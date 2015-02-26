#!/usr/bin/python
#..*..coding:utf-8 ..*..
### GTK+
from gi.repository import Gtk
from gi.repository import GdkPixbuf, GObject
### config file 
import config as c
##############
## Graphic library ##
##############
from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import random as r
import controlador as ctrl
import time,threading
import UTIL.configUtil as cfg

class App():
  def __init__(self):
    builder =Gtk.Builder()
    """ ******  I18N ********  """
    #builder.set_translation_domain('app')
    """ **********************  """
    builder.add_from_file("interfaz.glade")
    builder.connect_signals(self)
    self.window = builder.get_object("inicial")
    self.combobox_principal=builder.get_object("combobox_principal")
    #frame grafica
    self.frameCentral=builder.get_object("frame_contenedor")
    self.frameCentralTodo=builder.get_object("frame_contenedor_grande")
    self.frameCentralLabel=builder.get_object("label_contenedor_grafica")
    ##############
    self.box_lateral=builder.get_object("box_lateral_superior")
    self.listStore_companies=builder.get_object("liststore_company")
    self.treeView_companies=builder.get_object("treeview_company")
    self.comboBox_companies=builder.get_object("combobox_companies")
    self.comboBox_tiempo_mostrar=builder.get_object("combobox_tiempo_mostrar")
    self.box_cartera=builder.get_object("grid_cartera")
    self.box_previsiones=builder.get_object("box_previsiones")
    builder.get_object("linkbuttonGit").set_label("mandrewcito")
    self.label_ultima_actualizacion=builder.get_object("label_ultima_actualizacion")
    self.label_ultima_actualizacion.set_text("Ultima actualización "+cfg.getTag("config.ini","actualizacion","lastupdate"))
    self.label_version=builder.get_object("label_version")
    self.label_version.set_text(" v "+cfg.getTag("config.ini","app","version"))
    self.creaListStoreCompanies()
    self.companies_menu=[self.box_previsiones,self.comboBox_companies,self.comboBox_tiempo_mostrar,self.frameCentral,self.frameCentralLabel]
    self.cartera_menu=[self.box_cartera]
    self.progressBar=builder.get_object("barra_carga")
    self.progressBar.set_show_text(True)
    self.cargado=False
    self.window.show()

  def setTextProgressBar(self,w,texto):
    self.progressBar.set_text(texto)

  def on_cargaFinalizada(self,w):
    self.progressBar.set_fraction(0.0)
    self.setTextProgressBar(w,"actualizado")

  def on_cargando(self,w):
    self.progressBar.pulse()

  def on_cerrar_ventana(self,w,e):
    # en cerrar abrir dialogo esta seguro
    Gtk.main_quit()

  ''' operaciones con menu companies '''
  def ocultarMenuCompanies(self):
    for e in self.companies_menu:
      e.hide()

  #al cambiar de compañia cambiamos sus datos con los nuevos
  def on_combobox_companies_changed(self,w):
    company=self.comboBox_companies.get_model()[self.comboBox_companies.get_active()][0]
    tipo=self.comboBox_tiempo_mostrar.get_model()[self.comboBox_tiempo_mostrar.get_active()][0]
    fInicio=""
    fFin=""
    busq=ctrl.Busqueda(self)
    b0 = threading.Thread(target=busq.searchQuotes,args=(company,tipo,fInicio,fFin))
    b0.start()
    busq=ctrl.Busqueda(self)
    b1 = threading.Thread(target=busq.progressBar)
    b1.start()

  def mostrarMenuCompanies(self):
    for e in self.companies_menu:
      e.show()
  ''' END operaciones con menu companies '''

  def on_combobox_principal_changed(self,w):
    # escoge el modelo (filas), selcciona la activa, y elige la columna de la que queremos el texto
    opcion=self.combobox_principal.get_model()[self.combobox_principal.get_active()][0]
    if (opcion=="Compra"):
      self.mostrarMenuCompanies()
      valores = r.sample(range(50),  20)
      self.cargarEnContenedor(self.window,valores)
    else :
      self.ocultarMenuCompanies()

    if (opcion=="Cartera"):
      self.box_cartera.show()
    else:
      self.box_cartera.hide()

  def cargarEnContenedor(self,w,valores):
    canvas=self.creaGrafico(valores)
    GObject.idle_add(self.cargaContenido,canvas,self.frameCentral,0)
    
  #init store companies
  def creaListStoreCompanies(self):
    #self.listStore_companies.clear()
    #lo rellenamos con los valores 
    for valor in c.lista_company:
      self.listStore_companies.append([valor])

  ######################################### crear figura y hacer elemento canvas para GtK
  def creaGrafico(self,valores) : # llamara al controlador para pedir los datos, creara la figure y el grafico gtk
    #llamada al controlador para pedir los datos, parsear los que se obtienen de la interfaz etc
    fig=self.creaFigure('rectilinear',valores)# despues se le pasaran unos datos este es el ejemplo 
    return self.creaGraficoGtk(fig) #devuelve el elemento canvas creado
  
  def creaFigure(self,tipo_grafica,valores): 
    fig = Figure(dpi=50)
    #for *projection* are: ['aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear'].
    plt = fig.add_subplot(111, projection=tipo_grafica)
    plt.plot(valores)
    return fig

  def creaGraficoGtk(self,figure):
    # a partir de fig, creamos un elem canvas con el tam espeficicado
    x,y=self.window.get_size()
    canvas = FigureCanvas(figure)
    canvas.set_size_request(450,300)
    return canvas 
  #######################################################
  def actualizaLabel(self,label,contenido):
    label.set_text(contenido)
    label.show()

  def cargaContenido(self,contenido,contenedor,posicion):
    box1 = Gtk.HBox()
    box1.pack_start(contenido,True,True,posicion)
    for e in contenedor.get_children():
      contenedor.remove(e)
    contenedor.add(box1)
    #contenedor.set_child_packing(contenido,True,True,posicion,Gtk.PackType.START)
    contenedor.show_all()
    

GObject.threads_init()
App()
Gtk.main()	
