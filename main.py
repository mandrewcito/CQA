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
    #grafica 
    '''
    self.figure = Figure(figsize=(5,5), dpi=100)
    self.axis = self.figure.add_subplot(111, projection='polar')
    self.canvas = FigureCanvas(self.figure) # a gtk.DrawingArea
    self.canvas.show() 
    self.graphview = builder.get_object("plot") 
    self.graphview.pack_start(self.canvas, True, True, True)
    '''
    self.window.show_all()

  def on_cerrar_ventana(self,w,e):
    # en cerrar abrir dialogo esta seguro
    Gtk.main_quit()

  def on_combobox_principal_changed(self,w):
    # escoge el modelo (filas), selcciona la activa, y elige la columna de la que queremos el texto
    opcion=self.combobox_principal.get_model()[self.combobox_principal.get_active()][0]
    if (opcion=="Compra"):
      GObject.idle_add(self.cargarEnContenedor,self.window)

  def cargarEnContenedor(self,w):
    fig = Figure(figsize=(5,5), dpi=100)
    ax = fig.add_subplot(111, projection='polar')
    #grafico ejemplo
    N = 20
    theta = linspace(0.0, 2 * pi, N, endpoint=False)
    radii = 10 * random.rand(N)
    width = pi / 4 * random.rand(N)

    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
      bar.set_facecolor(cm.jet(r / 10.))
      bar.set_alpha(0.5)

    ax.plot()
    #grafico ejemplo
    canvas = FigureCanvas(fig)
    canvas.set_size_request(200,200)
    self.frameCentral.pack_start(canvas, True, True, 0)
    print "mostramos el grafico nuevo"
    w.show_all()

GObject.threads_init()
App()
Gtk.main()	
