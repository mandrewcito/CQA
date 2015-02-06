import ConfigParser

def getTag(file,section,property):
  config = ConfigParser.ConfigParser()
  config.read(file)
  return config.get(section,property)

def setTag(file,section,property,newValue):
  config = ConfigParser.ConfigParser()
  config.read(file)
  cfgfile = open(file,'w')
  config.set(section,property,newValue)
  config.write(cfgfile)
  cfgfile.close()
