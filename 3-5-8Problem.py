class digraph:
    def __init__(self):
        self.states={}
        self.operations=[]
        
class state:
    def __init__(self,x,y,z,parent):
        self.bottles=[x,y,z]
        self.code="%s %s %s"%(x,y,z)
        parent.states[self.code]=self
    
class operation:
    def __init__(self,inp,out,parent):
        self.source=inp
        self.target=out
        parent.operations.append(self)

def pourwater(source,target,i,grph):
    if target==0:
        limit=8
    if target==1:
        limit=5
    if target==2:
        limit=3
    if grph.states[i].bottles[source]!=0 and grph.states[i].bottles[target]!=limit:
        templist=list(filter(lambda x: True, grph.states[i].bottles))
        while True:
            if templist[source]!=0 and templist[target]!=limit:
                templist[source]-=1
                templist[target]+=1
            else:
                break
        tempcode="%s %s %s"%tuple(templist)
        operation(grph.states[i].code,tempcode,grph)    

pathslist=[]

def findpath(start,stop,grph,currentpath=[]):
    currentpath=list(filter(lambda x:True,currentpath))
    currentpath.append(start)
    if start==stop:
        pathslist.append(currentpath)
        return currentpath
    oplist=[]
    for i in grph.operations:
        if i.source==start and not start in currentpath[:-1]:
            oplist.append(i)
    for i in oplist:
        findpath(i.target,stop,grph,currentpath)
    
mygraph=digraph()

for i in range(4):
    for v in range(6):
        state(8-i-v,v,i,mygraph)

poplist=[]

for i in mygraph.states:
    if not (mygraph.states[i].bottles[0]==8 or mygraph.states[i].bottles[1]==5 or mygraph.states[i].bottles[2]==3 or mygraph.states[i].bottles[0]==0 or mygraph.states[i].bottles[1]==0 or mygraph.states[i].bottles[2]==0):
        poplist.append(i)
        
for i in poplist:
    mygraph.states.pop(i)
    
for i in mygraph.states:
    for v in range(3):
        for k in range(3):
            if v!=k:
                pourwater(v,k,i,mygraph)
                                
findpath("8 0 0","4 4 0",mygraph)

print("Best Path:")

shortestpath=pathslist[0]
for i in pathslist:
    if len(i)<len(shortestpath):
        shortestpath=i
        
print(shortestpath)
print("All Paths: ")
for i in pathslist:
    print(i)
    