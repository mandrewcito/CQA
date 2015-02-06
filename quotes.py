class Quote():
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,acompany,avalue):
    self._company=acompany
    self._value=avalue

class InstantQuote(Quote):
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,adate,acompany,avalue):
    Quote.__init__(self,acompany,avalue)
    self._type="InstantQuote"
    self._date=adate #dd/mm/yy-hh:mm

  def toDict(self):
    return {"type":self._type,"date":self._date,"company":self._company,"value":self._value}

  def getDate(self):
    return self._date

  def getType(self):
    return self._type

  def getCompany(self):
    return self._company

  def getValue(self):
    return self._value
    
class SumaryDayQuote(Quote):
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,adate,acompany,avalue,aVaration):
    Quote.__init__(self,acompany,avalue)
    self._type="SumaryDayQuote"
    self._date=adate#dd/mm/yy
    self._variation=aVariation # in %

  def toDict(self):
    return {"type":self._type,"date":self._date,"company":self._company,"value":self._value,"variation":self._variation}

  def getDate(self):
    return self._date

  def getType(self):
    return self._type

  def getCompany(self):
    return self._company

  def getValue(self):
    return self._value

  def getVariation():
    return self._variation
    
