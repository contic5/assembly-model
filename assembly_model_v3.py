import random
class Item():
    x=0.0
    y=0.0
    z=0.0
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.x=x
        self.y=y
        self.z=z
        super().__init__()
    def __str__(self):
        return "x="+str(self.x)+" y="+str(self.y)+" z="+str(self.z)
    def distance(self,other): #Returns distance between two items
        if(isinstance(other,Item)): #Checks if Item is valid
            result=((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)**0.5
            return result
        else:
            print("NOT OTHER")
            return None

class Part(Item):
    connectsto=[] #What part does this part connect to
    connectareas=[]
    isconstant=False
    weight=0.0
    length=0.0
    width=0.0
    height=0.0
    partid=0
    def __init__(self,partid=0,isconstant=False,x=0,y=0,z=0,weight=0,length=0,width=0,height=0):
        self.partid=partid
        self.isconstant=isconstant
        self.weight=weight
        self.length=length
        self.width=width
        self.height=height
        self.connectareas=[]
        super().__init__(x,y,z)
    def addconnect(self,newconnect):
        self.connectareas.append(newconnect)


class Connect(Item):
    partid=0
    def __init__(self,partid,x=0.0,y=0.0,z=0.0):
        self.partid=partid
        super().__init__(x,y,z)
    def __str__(self):
        return "id="+str(self.partid)+"x="+str(self.x)+" y="+str(self.y)+" z="+str(self.z)

class RobotArm(Item):
    movementspeed=5.0
    distancetraveled=0.0
    weightcarried=0.0
    curweightcarrying=0
    time=0
    def __init__(self,x=0.0,y=0.0,z=0.0):
        super().__init__(x,y,z)
    def movetopart(self,part,pickup=False):
        self.distancetraveled+=self.distance(part)
        if(pickup):
            self.curweightcarrying=part.weight
        else:
            self.weightcarried+=self.curweightcarrying
            self.curweightcarrying=0
        self.x=part.x
        self.y=part.y
        self.z=part.z
    def setpos(self,part):
        self.x=part.x
        self.y=part.y
        self.z=part.z

class HumanArm(Item):
    movementspeed=4.0
    distancetraveled=0.0
    weightcarried=0.0
    curweightcarrying=0
    time=0.0
    def __init__(self,x=0.0,y=0.0,z=0.0):
        super().__init__(x,y,z)
    def movetopart(self,part,pickup=False):
        self.distancetraveled+=self.distance(part)
        if(pickup):
            self.curweightcarrying=part.weight
        else:
            self.weightcarried+=self.curweightcarrying
            self.curweightcarrying=0
        self.x=part.x
        self.y=part.y
        self.z=part.z
    def movetoconnect(self,connect,pickup=False):
        self.distancetraveled+=self.distance(connect)
        if(pickup):
            self.curweightcarrying=part.weight
        else:
            self.weightcarried+=self.curweightcarrying
            self.curweightcarrying=0
        self.x=part.x
        self.y=part.y
        self.z=part.z
    def setpos(self,part):
        self.x=part.x
        self.y=part.y
        self.z=part.z

def rand(maxval):
    return random.random()*maxval

smallweight=
time=0 #How long it takes to finish task
botheaviestpriority=0
botclosestpriority=0
botfarthestpriority=100


humanlightestpriority=1
humanclosestpriority=100

humanarm=HumanArm(0,10,5)
robotarm=RobotArm(15,10,5)
parts=[]
base=Part(partid=4,isconstant=True,x=rand(10),y=0,z=rand(10),weight=30.0)
base.addconnect(Connect(partid=0,x=0,y=5,z=0))
base.addconnect(Connect(partid=1,x=0,y=5,z=10))
base.addconnect(Connect(partid=2,x=10,y=5,z=0))
base.addconnect(Connect(partid=3,x=10,y=5,z=10))
base.addconnect(Connect(partid=5,x=3,y=10,z=3))
base.addconnect(Connect(partid=6,x=3,y=10,z=8))
base.addconnect(Connect(partid=7,x=8,y=10,z=3))
#base.addconnect(Connect(partid=8,x=8,y=10,z=8))

parts.append(Part(partid=0,isconstant=False,x=rand(20),y=0,z=rand(20),weight=10.0))
parts.append(Part(partid=1,isconstant=False,x=rand(20),y=0,z=rand(20),weight=10.0))
parts.append(Part(partid=2,isconstant=False,x=rand(20),y=0,z=rand(20),weight=10.0))
parts.append(Part(partid=3,isconstant=False,x=rand(20),y=0,z=rand(20),weight=10.0))
parts.append(base)
parts.append(Part(partid=5,isconstant=False,x=rand(20),y=0,z=rand(20),weight=5.0))
parts.append(Part(partid=6,isconstant=False,x=rand(20),y=0,z=rand(20),weight=5.0))
parts.append(Part(partid=7,isconstant=False,x=rand(20),y=0,z=rand(20),weight=5.0))
#parts.append(Part(partid=8,isconstant=False,x=rand(20),y=0,z=rand(20),weight=5.0))
print(base.connectareas)
connectpart=[]
for i in range(len(parts)):
    part=parts[i]
    if(part.isconstant==True):
        connectpart.append(part)

parts.remove(connectpart[0])
while(len(parts)>0):
    bestpart=0
    bestpartscore=0
    nearestpartdistance=10000
    nearestpart=0
    farthestpartdistance=0
    farthestpart=0
    heaviestpartweight=0
    heaviestpart=0
    print("Robot Turn")
    for j in range(len(parts)):
        currentconnect=None
        for k in range(len(connectpart[0].connectareas)):
            if(j==k):
                currentconnect=connectpart[0].connectareas[k]
                break
        curdistance=robotarm.distance(parts[j])+parts[j].distance(currentconnect)
        if(curdistance<nearestpartdistance):
            nearestpartdistance=curdistance
            nearestpart=j
        if(curdistance>farthestpartdistance):
            farthestpartdistance=curdistance
            farthestpart=j
        if(parts[j].weight>heaviestpartweight):
            heaviestpartweight=parts[j].weight
            heaviestpart=j
    
    for j in range(len(parts)):
        partscore=1000
        currentconnect=None
        for k in range(len(connectpart[0].connectareas)):
            if(j==k):
                currentconnect=connectpart[0].connectareas[k]
                break
        curdistance=robotarm.distance(parts[j])+parts[j].distance(currentconnect)

        partscore=botfarthestpriority*(curdistance/farthestpartdistance)+botclosestpriority*(nearestpartdistance/curdistance)
        +botheaviestpriority*(parts[j].weight/heaviestpartweight)
        if(partscore>bestpartscore):
            bestpartscore=partscore
            bestpart=j

    part=parts[bestpart]
    bestconnect=None
    print("Best part is",part.partid)
    for k in range(len(connectpart[0].connectareas)):
        if(bestpart==k):
            bestconnect=connectpart[0].connectareas[k]
            break
    if(part.isconstant==False):
        part.connectsto.append(connectpart[0].partid)
        robotarm.movetopart(part,pickup=True)
        '''
        print("Grabbing part",part.partid)
        print("Distance traveled is",robotarm.distancetraveled)
        '''
        robotarm.movetopart(bestconnect,pickup=False)
        '''
        print("Moving part",part.partid,"to",connectpart[0].partid)
        print("Distance traveled is",robotarm.distancetraveled)
        '''
        parts.remove(part)
    
    if(len(parts)==0):
        break
    print("Human Turn")
    bestpart=0
    bestpartscore=0
    nearestpartdistance=10000
    nearestpart=10000
    heaviestpartweight=0
    heaviestpart=0
    for j in range(len(parts)):
        for k in range(len(connectpart[0].connectareas)):
            if(j==k):
                currentconnect=connectpart[0].connectareas[k]
                break
        curdistance=robotarm.distance(parts[j])+parts[j].distance(currentconnect)
        if(curdistance<nearestpartdistance):
            nearestpartdistance=curdistance
            nearestpart=j
        if(parts[j].weight>heaviestpartweight):
            heaviestpartweight=parts[j].weight
            heaviestpart=j

    for j in range(len(parts)):
        partscore=1000
        for k in range(len(connectpart[0].connectareas)):
            if(j==k):
                currentconnect=connectpart[0].connectareas[k]
                break
        curdistance=robotarm.distance(parts[j])+parts[j].distance(currentconnect)

        partscore=humanclosestpriority*(nearestpartdistance/curdistance)+humanlightestpriority*(parts[j].weight/heaviestpartweight)
        if(partscore>bestpartscore):
            bestpartscore=partscore
            bestpart=j
    part=parts[bestpart]

    bestconnect=None
    for k in range(len(connectpart[0].connectareas)):
        if(bestpart==k):
            bestconnect=connectpart[0].connectareas[k]
            break
    print("Best part is",part.partid)
    if(part.isconstant==False):
        part.connectsto.append(connectpart[0].partid)
        humanarm.movetopart(part,pickup=True)
        '''
        print("Grabbing part",part.partid)
        print("Distance traveled is",humanarm.distancetraveled)
        '''
        humanarm.movetopart(bestconnect,pickup=False)
        '''
        print("Moving part",part.partid,"to",connectpart[0].partid)
        print("Distance traveled is",humanarm.distancetraveled)
        '''
        parts.remove(part)

print("Robot total distance traveled is",robotarm.distancetraveled)
print("Robot total weight carried is",robotarm.weightcarried)
print("Human total distance traveled is",humanarm.distancetraveled)
print("Human total weight carried is",humanarm.weightcarried)