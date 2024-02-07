class StatsData:
  def __init__(self):
    self.latviar=[19.1,17.8,15.5,18.2,16.7,23.2,19.2,22.9,21.8,14.2,32.2,21.9,15.8,38.8,34.3,23.3,15.2,37.3,32.7,23.9,15.6,30.7,30.4,22.6,18.6]
    self.lietuvar=[12,12.3,12.6,13.3,14.7,17.3,17.9,19.4,19.9,21,21.5,22,23.9,24.1,24.1,24.2,24.9,25.1,25.3,26.6,26.7,27.1,27.9,29.2,31.5,33,33.3,33.6,36]
    self.estir=[23.3,24.3,24.4,24.6,24.9,25.2,25.5,25.5,25.6,26.1,30.9,32,33.2,35.9,37.5,40.3,42.7,44.6,44.6,45.9,48,49.6,51.7,51.9]

  def getVidejaijsl(self):
    return(sum(self.latviar) / len(self.latviar))
  def getVidejaijslit(self):
    return(sum(self.lietuvar) / len(self.lietuvar))
  def getVidejaijsest(self):
    return(sum(self.estir) / len(self.estir))