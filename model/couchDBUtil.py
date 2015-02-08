def dateToCouchDBDate(fecha):
  #"1971-01-01T00:00:00Z"
  fecha=fecha.split("-")
  f1=fecha[0].split("/")
  f2=fecha[1].split(":")
  dateCouchDB="{0}-{1}-{2}T{3}:{4}:00Z".format(f1[2],f1[1],f1[0],f2[0],f2[1]).replace(" ", "")
  return dateCouchDB

def couchDBDateToDate(fecha):
  fecha=fecha.split("T")
  f1=fecha[0].split("-")
  f2=fecha[1].split(":")
  date="{0}/{1}/{2}-{3}:{4}".format(f1[2],f1[1],f1[0],f2[0],f2[1]).replace(" ", "")
  return date
