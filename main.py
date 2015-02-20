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
    self.frameCentral=builder.get_object("frame_contenedor")
    self.box_lateral=builder.get_object("box_lateral_superior")
    self.listStore_companies=builder.get_object("liststore_company")
    self.treeView_companies=builder.get_object("treeview_company")
    self.comboBox_companies=builder.get_object("combobox_companies")
    self.comboBox_tiempo_mostrar=builder.get_object("combobox_tiempo_mostrar")
    self.creaListStoreCompanies()
    companies_menu=[self.comboBox_companies,self.comboBox_tiempo_mostrar]
    self.window.show()
    self.companies_menu=companies_menu

  def on_cerrar_ventana(self,w,e):
    # en cerrar abrir dialogo esta seguro
    Gtk.main_quit()

  ''' operaciones con menu companies '''
  def ocultarMenuCompanies(self):
    for e in self.companies_menu:
      e.hide()

  def mostrarMenuCompanies(self):
    for e in self.companies_menu:
      e.show()
  ''' END operaciones con menu companies '''

  def on_combobox_principal_changed(self,w):
    # escoge el modelo (filas), selcciona la activa, y elige la columna de la que queremos el texto
    opcion=self.combobox_principal.get_model()[self.combobox_principal.get_active()][0]
    if (opcion=="Compra"):
      self.mostrarMenuCompanies()
      self.cargarEnContenedor(self.window)
    else :
      self.ocultarMenuCompanies()

  def cargarEnContenedor(self,w):
    canvas=self.creaGrafico()
    GObject.idle_add(self.cargaContenido,canvas,self.frameCentral,0)
    
  #init store companies
  def creaListStoreCompanies(self):
    #self.listStore_companies.clear()
    #lo rellenamos con los valores 
    for valor in c.lista_company:
      self.listStore_companies.append([valor])

  ######################################### crear figura y hacer elemento canvas para GtK
  def creaGrafico(self) : # llamara al controlador para pedir los datos, creara la figure y el grafico gtk
    #llamada al controlador para pedir los datos, parsear los que se obtienen de la interfaz etc
    valores = r.sample(range(50),  20)
    fig=self.creaFigure('rectilinear',valores)# despues se le pasaran unos datos este es el ejemplo 
    return self.creaGraficoGtk(fig) #devuelve el elemento canvas creado
  
  def creaFigure(self,tipo_grafica,valores): 
    fig = Figure(dpi=50)
    #for *projection* are: ['aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear'].
    plt = fig.add_subplot(111, projection=tipo_grafica)
    plt.plot(valores)
    return fig

  def creaGraficoGtk(self,figure): #devuelve canvas obj poner TODO alto y ancho despues 
    # a partir de fig, creamos un elem canvas con el tam espeficicado
    canvas = FigureCanvas(figure)
    canvas.set_size_request(500,300)
    return canvas 
  #######################################################

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
