from datetime import datetime

def dateSplit(date):
  fecha=date.split("-")
  f1=fecha[0].split("/")
  f2=fecha[1].split(":")
  return int(f1[0]),int(f1[1]),int(f1[2]),int(f2[0]),int(f2[1])

def esMasReciente(fechaActualizacion,lastUpdate):
  d,m,y,h,mi=dateSplit(fechaActualizacion)
  t1=datetime(y,m,d,h,mi)
  d,m,y,h,mi=dateSplit(lastUpdate)
  t2=datetime(y,m,d,h,mi)
  return t1>t2
