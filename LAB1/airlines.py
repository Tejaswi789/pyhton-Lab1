class Person():
    # define constructor with parameters: name,email,age,phonenumber,ssn
    def __init__(self,firstname,lastname,emailaddress,phonenumber,age,ssn):
        self.fname=firstname
        self.lname=lastname
        self.email=emailaddress
        self.pnum=phonenumber
        self.age=age
        self.ssn=ssn
    # prints name of person
    def getname(self):
        print("    Name:  {} {}".format(self.fname, self.lname))

    # age of person
    def getage(self):
           print("    Age:  ",self.age)

    # Phone number

    def getnumber(self):
           print("    Phone no: " +self.pnum)

    # Email
    def getemail(self):
        print("    Email:",self.email)

    # define Private Member
    def __getssn_(self):
        print("    SSN",self.ssn)

# Define Flight details
class FlightDetails():
    # define init constructor
    def __init__(self,flight_num,flight_name):
        self.flightnum=flight_num
        self.flightname=flight_name

    # print airlines
    def getairlinesname(self):
        print("    Airlines: ",self.flightname)
    # Flight no.
    def getflightno(self):
        print("    FlightNo:",self.flightnum)

# define Seating Allotment class
class SeatingAllotment():
    # def constructor
    def __init__(self, seatnum,seatletter):
        self.snum=seatnum
        self.sletter=seatletter
    # print Seating details
    def getseatinfo(self):
        print("    Seating details:",self.snum,self.sletter)


# Inheriting SeatAllotment class
class Booking(SeatingAllotment):
    # define constructor
    def __init__(self,travelclass, deptdate, source,destination,depttime,seatnum,seatletter):
        SeatingAllotment.__init__(self,seatnum,seatletter)
        self.travelclass=travelclass
        self.deptdate=deptdate
        self.source=source
        self.dest=destination
        self.depttime=depttime
        self.seatnum = seatnum
        self.seatletter = seatletter

    def gettravelclass(self):
        print("    Class :",self.travelclass)

    def getsource(self):

        print("    Source :", self.source)

    def getdest(self):
        print("    Destination :", self.dest)

    def getdepttime(self):
        print("    Department Time:", self.depttime)

    def getdepdate(self):
        print("    Departure Date:",self.deptdate)

# Multiple Inheritance ( Passenger class inherits Person, FlightDetails, Booking)
class Passenger(Person, FlightDetails, Booking):

    def __init__(self,firstname,lastname,emailaddress,phonenumber,age,ssn,flight_num,
                 flight_name,travelclass, deptdate,depttime, source, destination,seatnum, seatletter):
        # Super() keyword
        super(Passenger,self).__init__(firstname, lastname, emailaddress, phonenumber, age, ssn)  # super keyword used
        # Calling the Booking class
        Booking.__init__(self,travelclass, deptdate, source,destination,depttime,seatnum,seatletter)
        # Calling the FlightDetails class
        FlightDetails.__init__(self, flight_num,flight_name)

# passing the parameters
t = Passenger("Tejaswi","Ayyadapu","atgkp@gmail.com",
              "8164822556",18,"3442","aaaaa","AmericanAirlines","Economy","Jun 15","23.30", "USA","india",27,'A')
print(" ____________________________________")
print("|  Passenger Details:                |")
print(" ____________________________________")
t.getname()
t.getemail()
t.getage()
t.getnumber()
print(" ____________________________________")