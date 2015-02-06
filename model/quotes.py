class Quote():
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,acompany,avalue):
    self._company=acompany
    self._value=avalue

  def getCompany(self):
    return self._company

  def getValue(self):
    return self._value

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

    
class SumaryDayQuote(Quote):
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,adate,acompany,avalue,aVaration):
    Quote.__init__(self,acompany,avalue)
    self._type="SumaryDayQuote"
    self._date=adate#dd/mm/yy
    self._variation=aVariation # in %, diferente between first and last InstantQuote of the day  

  def toDict(self):
    return {"type":self._type,"date":self._date,"company":self._company,"value":self._value,"variation":self._variation}

  def getDate(self):
    return self._date

  def getType(self):
    return self._type

  def getVariation():
    return self._variation


class SumaryMonthQuote(Quote):
  #We use this obj for creating DB documents (valueObjects)
  def __init__(self,adate,acompany,avalue,aVaration):
    Quote.__init__(self,acompany,avalue)
    self._type="SumaryMonthQuote"
    self._date=adate#dd/mm
    self._variation=aVariation # in %,diferente between first and last SumaryDayQuote of the month

  def toDict(self):
    return {"type":self._type,"date":self._date,"company":self._company,"value":self._value,"variation":self._variation}

  def getDate(self):
    return self._date

  def getType(self):
    return self._type

  def getVariation():
    return self._variation
    
