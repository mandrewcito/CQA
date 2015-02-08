#!/usr/bin/python
#..*..coding:utf-8 ..*..

from gi.repository import Gtk
from gi.repository import GdkPixbuf, GObject

class App():
  def __init__(self):
    builder =Gtk.Builder()
    """ ******  I18N ********  """
    #builder.set_translation_domain('app')
    """ **********************  """
    builder.add_from_file("interfaz.glade")
    builder.connect_signals(self)
    self.window = builder.get_object("principal")
    self.listStoreCompany=builder.get_object("liststore_company")
    self.window.show_all()

  def saludo(self,w):
    #self.listStoreCompany.clear()
    self.listStoreCompany.append(["pene"])

  def on_cerrar_ventana(self,w,e):
    # en cerrar abrir dialogo esta seguro
    Gtk.main_quit()

GObject.threads_init()
App()
Gtk.main()	
