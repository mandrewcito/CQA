#CutreQuoteAnalyzer

##Requirements

Python 2.7.3, CouchDB(and python-couchdb)
---
## init

* fill database -> Execute ibexQuery.py with cron
([how to configure cron](http://www.codigonomada.com/como-anadir-tareas-programadas-con-cron-linux/))
* DB -> couchDB, getDao.DaoUtil() -> for DB operations
---
**TODO:**
* API yahoo (or similar)
* Organize classes
* graphics
* model Queries
* config / automatizacion de consulta pagina en RAW(asistente)
* hacer Doc resumen de cada compañia al dia (asi borramos las cotizaciones instantaneas para ahorrar espacio)
---
##Tiempos

UTIL/medidas/medirTiempo.py PROGRAMA - mide tiempo ejecución de PROGRAMA

###insercion

consulta a pagina + procesado + guardar en BD (otro pc) -> 14 sec(fuerza bruta descargando la pagina en RAW)

---
##Queries

With couchdb views
[wiki](http://wiki.apache.org/couchdb/Introduction_to_CouchDB_views),[tutorial](http://guide.couchdb.org/draft/views.html)

###recuperar documentos en un determinado intervalo de tiempo

###recuperar un documentos de una empresa dada en un intervalo de tiempo

###recuperar un documentos de todas las empresas en un intervalo de tiempo
---
