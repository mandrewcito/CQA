class Quote():
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,adate,acompany,avalue):
    self._type="InstantQuote"
    self._date=adate
    self._company=acompany
    self._value=avalue

  def toDict(self):
    return {"type":self._type,"date":self._date,"company":self._company,"value":self._value}

  def getDate():
    return self._date

  def getType():
    return self._type

  def getCompany():
    return self._company

  def getValue():
    return self._value
    
