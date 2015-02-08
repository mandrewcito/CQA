#CutreQuoteAnalyzer

##Requirements

Python 2.7.3, CouchDB(and python-couchdb)

---
## init

* fill database -> Execute ibexQuery.py with cron
([how to configure cron](http://www.codigonomada.com/como-anadir-tareas-programadas-con-cron-linux/))
* DB -> couchDB, getDao.DaoUtil() -> for DB operations

---
## Dates

Dates are in format dd/mm/yyyy-hh:mm

---
**TODO:**

* API yahoo (or similar)
* Organize classes
* graphics(matlib)
* model Queries
* config / automatizacion de consulta pagina en RAW(asistente)
* hacer Doc resumen de cada compañia al dia (asi borramos las cotizaciones instantaneas para ahorrar espacio)
* insertar plot matlib en GTK

---
##Tiempos

UTIL/medidas/medirTiempo.py PROGRAMA - mide tiempo ejecución de PROGRAMA

###insercion

consulta a pagina + procesado + guardar en BD (otro pc) -> 14 sec(fuerza bruta descargando la pagina en RAW)

---
##Queries

With couchdb views
[wiki](http://wiki.apache.org/couchdb/Introduction_to_CouchDB_views),[tutorial](http://guide.couchdb.org/draft/views.html)

### Casos de uso :



---
