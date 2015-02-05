#CutreQuoteAnalyzer
##Requirements : Python 2.7.3, CouchDB(and python-couchdb)
fill database -> Execute ibexQuery.py with cron
([how to configure cron](http://www.codigonomada.com/como-anadir-tareas-programadas-con-cron-linux/))
DB -> couchDB, getDao.DaoUtil() -> for DB operations

**TODO:**
*API yahoo (or similar)
*Organize classes
*graphics
*model Queries
*config / automatizacion de consulta pagina en RAW(asistente)
*actualizar fecha cuando se inserta en BD

#Tiempos
UTIL/medidas/medirTiempo.py PROGRAMA - mide tiempo ejecución de PROGRAMA
##insercion
consulta a pagina + procesado + guardar en BD (otro pc) -> 14 sec(fuerza bruta descargando la pagina en RAW)
##recuperar documentos en un determinado intervalo de tiempo
##recuperar un documentos de una empresa dada en un intervalo de tiempo
##recuperar un documentos de todas las empresas en un intervalo de tiempo
