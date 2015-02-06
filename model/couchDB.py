# --*-- coding: utf-8 --*--

import sys
import locale
import uuid
import couchdb
import quotes
import mapFun
# couchdb doc says:
#
# "Note that it is generally better to avoid saving documents with no
#  _id and instead generate document IDs on the client side. This is
#  due to the fact that the underlying HTTP POST method is not
#  idempotent, ..."
#
#  and
#
# "The save() method creates a document with a random ID generated by
#  CouchDB (which is not recommended)."
#
# so
# We assign an id during document instantiation, using uuid module.
#
# "uuid4() generates, as you said, a random UUID. The chance of
# a collision is really, really, really small."
# We'll live with it.
#couchDB.server(c.serverDir)[db]

class CouchDBDAO:
  def __init__(self,db):
    self._db=db

  def insert(self,doc):
    """
    Añadir un documento a la BD.
    @param doc: El documento a insertar.
    @type  doc: CouchdbVO
    """
    return self._db.create(doc)
    #print >>sys.stderr, u"INSERT({0}): {1}".format(self._db.name, doc).encode(locale.getpreferredencoding())

  def update(self,doc):
    """
    Actualizar un documento en la BD.
    @param doc: El documento a actualizar.
    @type  doc: CouchdbVO
    """
    self._db[doc.id] = doc
    #print >>sys.stderr, u"UPDATE({0}): {1}".format(self._db.name, doc).encode(locale.getpreferredencoding())

  def delete(self,doc):
    """
    Borrar un documento de la BD.
    @param doc: El documento a borrar.
    @type  doc: CouchdbVO
    """
    del self._db[doc.id]
    #print >>sys.stderr, u"DELETE({0}): {1}".format(self._db.name, doc).encode(locale.getpreferredencoding())

  def findByDate(self,date):
    #dada una fecha(dd/mm/yy), devuelve los documentos de esa fecha(cootizaciones)
    pass

  def findInstantQuoteByCompany(self,company,startDate,endDate):
    #devuelve lista de pares cootizacion fecha entre dos fechas dadas de una company
    #formateamos la consulta
    mf=mapFun.mfInstantQuote.format(company)
    #hacemos la consulta
    rows=self._db.query(mf)
    newquotes=[]
    for row in rows:
      newquotes.append(quotes.InstantQuote(row.key['company'],row.key['date'],row.key['value']))
    return newquotes

  def findDoc(self,doc):
    #devuelve ID doc dado un documento 
    pass

class CouchdbVO(couchdb.client.Document):
  """
  Value Object para CouchDB.  
  CouchDB maneja documentos que son listas de campos nombre,valor
  por lo que el mapping con los VOs es directo. El campo 'type' se
  usa para el tipo de objeto.El id lo creamos nosotros (explicacion arriba)
  """
  def __init__(self, **kwargs):
    doc=couchdb.client.Document.__init__(self, **kwargs)
    self['_id']=uuid.uuid4().hex


class InstantQuoteVO(CouchdbVO):
  """
  Instant quote of a company.
  """
  def __init__(self,aDate,aCompany,aValue):
    #date DD/MM/YY-hh:mm:ss
    CouchdbVO.__init__(self,type='InstantQuote',date=aDate,company=aCompany,value=aValue)




									
