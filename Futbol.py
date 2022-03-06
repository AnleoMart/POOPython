class person():
  def __init__(self, position, age, name, lastname, Nationality):
    self.position= position
    self.age= age
    self.name= name
    self.lastname= lastname
    self.Nationality= Nationality
  def describe_me(self):
    print("I am a " + self.name + " " + self.lastname + " I'm working as " + self.position + "my nationality is " + self.Nationality)
  def adult(self):
    if self.age >= 19:
      print("you are ", self.age, "Year old") 
  def toWalk(self):
    print("The", self.position , "are walking around soccer field" )
  def toRun (self):
    print("The", self.position , "are running around soccer field" )
  def toStatic (self):
    print("The", self.position , "are static on the soccer field" )
  def toJump (self):
    print("The", self.position , "are jumpping around soccer field" )
  def toRun (self):
    print("The", self.position , "are running around soccer field" )
  def toHead (self):
    print("The", self.position , "are head the ball around soccer field" )  

class player(person):
  def player_data(self):
    self.Number=int(input("Enter the NumerPlayer:"))
    print("My number is ",self.Number)
    #print("My number is " + self.Number + " injured " + self.injured)

class referee(person):
  def toLack(self):
    print("The referee penalizes any dangerous act or acts not valid in the regulations.")

class Ball():
  def __init__ (self, circunference, material, weight,pressure):
    self.circunference= circunference
    self.material= material 
    self.weight= weight
    self.pressure= pressure
  def toJump (self):
    print("The ball are jumpping around soccer field" )
  def toRoll (self):
    print("The ball are roll around soccer field" ) 

class team():
  def __init__(self, nameTeam, NatioTeam,):
    self.nameTea= nameTeam
    self.NatioTeam= NatioTeam
  def infoTeam(self):
    print("this is a small information about our team " + self.nameTea + " our team is " + self.NatioTeam)

class SoccerField():
  def __init__ (self, width, length, name, ubication, material):
    self.width= width
    self.length= length
    self.name= name
    self.ubication= ubication
    self.material= material

class technicalTeam(person):
  def __init__(self, position, age, name, lastname, Nationality, Job):
    self.Job= Job
    super().__init__(position, age, name, lastname, Nationality)
    print(position, age, name, lastname, Nationality) 

class Sub(person):
  pass

class GoalKeeper(person):
    def toTackle (self):
      print("The", self.position , "are tackle in the  soccer field" )

My_referee = referee("Referee", 23,"Leonardo", "Pulido", "Colonviano")
My_referee.describe_me()
My_referee.adult()
My_player= player("Forward",24, "Andres" , "Martínez","Colonviano")
My_player.describe_me()
#My_player.player_data()
My_team= team(" Pichonarios", "Chibchonvianos")
My_team.infoTeam()
technicalTeam=technicalTeam("technicalTeam", 23, "Anleo", "PulMart", "Colombiano", "Director tecnico")