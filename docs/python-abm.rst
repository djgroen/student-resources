
*************************************************************
Designing and prototyping your own simulation using Python 3.
*************************************************************

Written by Derek Groen (Derek.Groen@brunel.ac.uk)

In this tutorial, you will learn how to write a very basic agent-based simulation application. The example we use is a very simplistic simulation that attempts to predict the movement of refugees during the Northern Mali Conflict in 2012.

The underlying technique we introduce here is more widely known as *agent-based modelling*, or ABM.

==============================
What is agent-based modelling?
==============================

Types of agents

When thinking about refugee movements, there are a few basic elements:

    The refugees themselves.
    The locations where the refugees reside
    And possibly the paths (or routes) that interconnect the locations

In its simplest form, this agent-based model features refugees that reside at a
given location, and that move from one location to another as the time in the
simulation progresses.  Network-based versus geographically pixelated

In general there are two widespread basic approaches to ABM. One is
network-based, where each location is an agent, and the location agents are
interlinked using path agents. A second approach is geographically pixelated,
where a region is subdivided into square areas, and the location of agents is
indicated by the respective coordinates of the corresponding square areas.  The
code

What follows is a detailed investigation of the simulation code. The code works
as is, but as part of this tutorial you're being asked to change some of its
features from simplistic to something a bit more fancy.  

Imports
::
  import random

In this tutorial we use very few dependencies, but the random library is an
essential one, as agent-based simulations strongly rely on randomizers.

------------------------
Defining a single person
------------------------

We first start by defining a simple class which describes a refugee. Let's name
this class "Person", so that we could choose to reuse the class for other
simulation purposes.
::
  class Person:
    def __init__(self, location):
      self.ill = False
      self.injured = False
  
      self.age = 35
      self.location = location
      self.location.numAgents += 1

      # Set to true when an agent resides on a link.
      self.travelling = False


I gave the Person class a simple constructor (see the _init_() function), which
sets a number of parameters specific to the class. You can define any parameter
you like, but I opted for the following (semi-arbitrary) set:

* healthy: which indicates whether a Person is generally healthy or ill/weakened.
* injured: which indicates whether a Person is physically injured or not.
* age: age in years.
* location: a reference to the location where the Person currently resides.
* travelling: whether the Person is currently in transit, or stationary at one of the locations.

Now each Person will have to make decisions at different moment. In this code,
we model two types of decisions:

* Whether the Person wishes to move from its current location to another one.
* If 1 is the case: which route the Person will choose from a set of routes.

We will start with decision 2, which is at the lowest level, and create a
simple function that picks a favourite route amongst a list of routes. To do
this, we created a simple weighted choice algorithm:
::
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
    


Here, each option has a weight equal to 40000 (the approximate circumference of
the planet in km) divided by (10 + [distance to the endpoint of the route in
km]).

Because the function is rather simple, I included a full implementation.
However, the exact same functionality can also be accomplished using
numpy.random.choice().

selectRoute() is embedded in a more general function (evolve()), which evolves
the position of a Person over a single timestep in the simulation. This
function essentially captures the mechanics in making decision 1, and relies on
the aforementioned selectRoute() to resolve decision 2 when necessary:
::
  def evolve(self):
    movechance = self.location.movechance
    outcome = random.random()
    self.travelling = False
    if outcome < movechance:
      # determine here which route to take?
      chosenRoute = self.selectRoute()

      # update location to link endpoint
      self.location.numAgents -= 1
      self.location = self.location.links[chosenRoute]
      self.location.numAgents += 1
      self.travelling = True


Here the chance of a Person moving at all at a given time step is given by the
movechance. This movechance is a static number for each Location, allowing us
to set a high movechance for unsafe locations, and a lower movechance for safer
locations.

evolve() places Persons on the Links. To ensure that these Persons reach there
destination we create one more function, namely finish_travel()
::
  def finish_travel(self):
    if self.travelling:
      # update location (which is on a link) to link endpoint
      self.location.numAgents -= 1
      self.location = self.location.endpoint
      self.location.numAgents += 1 



This function is a little redundant right now (it could be part of evolve()),
but it allows you to later modify the code, to accomodate Persons to spend more
than one time step in transit.

======================
Defining the Locations
======================

Now Persons will reside at a given place, or Location. To define these places
in a networked model, we create a Location object for each place:
::
  class Location:
    def __init__(self, name, x=0.0, y=0.0, movechance=0.001):
      self.name = name
      self.x = x
      self.y = y
      self.movechance = movechance
      self.links = []
      self.numAgents = 0


The Location class, too, has a number of simple parameters. These represent essential characteristics for individual locations:

* name: the name of the Location.
* x: GPS x-coordinate, useful for placing on a map and for calculating distances as the bird flies.
* y: GPS y-coordinate.
* movechance: An indicator denoting the safety level of this location. Are refugees certain to stay put (0), certain to move out immediately (1) or will there be a mixture (0<movechance<1).
* links: An array containing routes/links/paths to other Locations.
* numAgents: A tracking variable that keeps count as to how many refugees are present at this Location.

==================
Defining the Links
==================

Another ingredient of our simulations is to interconnect our locations.
Geographically-resolved models represent each Location by a pixel, but in our
network-based model it is not immediately clear that give Locations are
adjacent. To define adjacencies, we therefore create Link objects which
interconnect a set of two locations:
::
  class Link:
    def __init__(self, endpoint, distance):

      # distance in km.
      self.distance = float(distance)

      # links for now always connect two endpoints
      self.endpoint = endpoint

      # number of agents that are in transit.
      self.numAgents = 0   


The Links class is accompanied with the following attributes:

* distance: The length of the link in kilometers.
* endpoint: A reference to the Location to which this Link will lead.
* numAgents: Our all-familiar tracking variable that keeps count as to how many refugees are in transit on this link.

Note: As Links are stored in arrays as part of each (starting) Location, we do not need to define the starting Location as a parameter of this class.

========================
From state to simulation
========================

We now have people, locations, and links that represent connections between
these locations. These are essential components for an agent-based model in
this context. It's easy to think up many other possible components (e.g.,
conflict events, other types of agents, more parameters regarding age, religion
etc.), but most of these are not essential for the simulation in its most basic
form. However, what is essential is to be able to model a period of time, i.e.
turning out frozen state into a simulation.

To accomplish this, we create an Ecosystem class, which stores the full state
(Locations, Links and Persons), and which is able to evolve them in time. We
define the class as follows:
::
  class Ecosystem:
    def __init__(self):
      self.locations = []
      self.locationNames = []
      self.agents = []
      self.time = 0


The Ecosystem class has the following attributes:

* locations: Contains all the locations in our system.
* locationNames: A shorthand list of the names of the respective locations in our system, to make it easier to write diagnostic information.
* agents: A list of all the agents in our system.
* time: Basically a clock, which contains the number of time steps that have been taken.

Next, we need a function that adds locations to the Ecosystem:
::
  def addLocation(self, name, x="0.0", y="0.0", movechance=0.1):
    l = Location(name, x, y, movechance)
    self.locations.append(l)
    self.locationNames.append(l.name)
    return l


...a function that adds Agents to the Ecosystem:
::
  def addAgent(self, location):
    self.agents.append(Person(location))


...and a function that adds Links to the Ecosystem:
::
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


Crucially, we want to evolve the system in time. This is actually done using the following function:
::
  def doTimeStep(self):
    #update agent locations
    for a in self.agents:
      a.evolve()

    for a in self.agents:
      a.finish_travel()

    #update link properties

    self.time += 1


Lastly, we add two functions to aid us in writing out some results.
::
  def numAgents(self):
    return len(self.agents)

  def printInfo(self):

    print("Time: ", self.time, ", # of agents: ", len(self.agents))
    for l in self.locations:
      print(l.name, l.numAgents)


=============================================
Creating and running a Agent-based Simulation
=============================================

We have now created all the essential classes to perform an agent-based
simulation. Here we describe how you can construct and run a simple ABM
simulation. We start off by creating an Ecosystem, and adding a source, and two
sink locations to it:
::
  if __name__ == "__main__":
    print("A first ABM implementation")

    e = Ecosystem()

    l1 = e.addLocation("Source")
    l2 = e.addLocation("Sink1")
    l3 = e.addLocation("Sink2")

Next, we establish two paths, each of which connects the source location to one
of the two sink locations. As a test, we specify one of the paths to have a
length of 10 kilometers, and one to have a length of 5 kilometers:
::
    e.linkUp("Source","Sink1","10.0")
    e.linkUp("Source","Sink2","5.0")


With the location and links in place, we can now insert a hundred agents in the
source location l1. To do that, we use the addAgent() function a hundred times.
::
    for i in range(0,100):
      e.addAgent(location=l1)


With all the agents in place, we can now proceed to run the simulation. We run
the simulation for a duration of 10 time steps, and we print basic diagnostic
information after each time step:
::
    duration=10
    for t in range(0,duration):
      e.doTimeStep()
      e.printInfo()


...and with that all in place, you have just established your first working ABM
model!
