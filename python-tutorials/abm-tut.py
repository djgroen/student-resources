import random

class Person:
  def __init__(self, location):
    self.ill = False
    self.injured = False
    self.x = 0.0
    self.y = 0.0

    self.age = 35
    self.location = location
    self.location.numAgents += 1

    # Set to true when an agent resides on a link.
    self.travelling = False
    self.distance_travelled_on_link = 0
    
    def selectRoute(self):
      total_score = 0.0
      for i in range(0,len(self.location.links)):
        total_score += 40000.0 / (10.0 + self.location.links[i].distance)

      selected_value = random.random() * total_score

      checked_score = 0.0
      for i in range(0,len(self.location.links)):
        checked_score += 40000.0 / (10.0 + self.location.links[i].distance)
        if selected_value < checked_score:
          return i
        
    def evolve(self):

      if not self.travelling:
        movechance = self.location.movechance
        outcome = random.random()

        if outcome < movechance:
          # determine here which route to take?
          chosenRoute = self.selectRoute()

          # update location to link endpoint
          self.location.numAgents -= 1
          self.location = self.location.links[chosenRoute]
          self.location.numAgents += 1
          self.travelling = True
         
  def finish_travel(self):
    # if the person resides on a link between locations, it is "travelling"
    if self.travelling:

      # increment the distance covered by 10 kilometers.
      self.distance_travelled_on_link += 10

      # get the length of the current route (link).
      link_length = self.location.distance

      # If the distance travelled is longer than the length of the link, we arrive at our destination.
      if self.distance_travelled_on_link > link_length:
        self.location.numAgents -= 1
        self.location = self.location.endpoint
        self.location.numAgents += 1
        self.travelling = False
        
class Location:
  def __init__(self, name, x=0.0, y=0.0, movechance=0.001):
    self.name = name
    self.x = x
    self.y = y
    self.movechance = movechance
    self.links = []
    self.numAgents = 0
    
class Link:
  def __init__(self, endpoint, distance):

    # distance in km.
    self.distance = float(distance)

    # links for now always connect two endpoints
    self.endpoint = endpoint

    # number of agents that are in transit.
    self.numAgents = 0
    
class Ecosystem:
  def __init__(self):
    self.locations = []
    self.locationNames = []
    self.agents = []
    self.time = 0
    
  def addLocation(self, name, x="0.0", y="0.0", movechance=0.1):
    l = Location(name, x, y, movechance)
    self.locations.append(l)
    self.locationNames.append(l.name)
    return l
  
  def addAgent(self, location):
    self.agents.append(Person(location))
    
  def linkUp(self, endpoint1, endpoint2, distance="1.0"):
    """ Creates a link between two endpoint locations
    """
    endpoint1_index = 0
    endpoint2_index = 0
    for i in range(0, len(self.locationNames)):
      if(self.locationNames[i] == endpoint1):
        endpoint1_index = i
      if(self.locationNames[i] == endpoint2):
        endpoint2_index = i

    self.locations[endpoint1_index].links.append( Link(self.locations[endpoint2_index], distance) )
    self.locations[endpoint2_index].links.append( Link(self.locations[endpoint1_index], distance) )
    
  def doTimeStep(self):
    #update agent locations
    for a in self.agents:
      a.evolve()

    #update agent travel on links
    for a in self.agents:
      a.finish_travel()

    self.time += 1
    
  def numAgents(self):
    return len(self.agents)

  def printInfo(self):

    print("Time: ", self.time, ", # of agents: ", len(self.agents))
    for l in self.locations:
      print(l.name, l.numAgents)

    my_file = open("agents.%s.csv" % (self.time), "w")

    my_file.write("#id,x,y\n")
    for id,a in enumerate(self.agents):
      my_file.write("%s,%s,%s\n" % (id, a.x, a.y))
    my_file.close()
    
if __name__ == "__main__":
  print("A first ABM implementation")

  e = Ecosystem()

  l1 = e.addLocation("Source1",x=200,y=0)
  l2 = e.addLocation("Source2",x=100,y=100)
  l3 = e.addLocation("Transit1",x=100,y=0)
  l4 = e.addLocation("Transit2",x=200,y=100)
  l5 = e.addLocation("Sink1",x=300,y=0)
  l6 = e.addLocation("Sink2",x=0,y=100)
  
  e.linkUp("Source1","Transit1","100.0")
  e.linkUp("Source1","Transit2","50.0")
  e.linkUp("Source2","Transit1","100.0")
  e.linkUp("Source2","Transit2","50.0")
  e.linkUp("Transit1","Sink1","200.0")
  e.linkUp("Transit2","Sink2","200.0")
  
  for i in range(0,100):
    e.addAgent(location=l1)
    
  duration=10
  for t in range(0,duration):
    e.doTimeStep()
    e.printInfo()
    
  
