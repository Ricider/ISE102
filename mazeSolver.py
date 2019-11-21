maze=[[1,0,1,0,0,0,0],
      [0,0,0,0,1,0,1],
      [1,1,1,0,1,0,1],
      [1,0,1,0,1,0,1],
      [1,0,0,0,1,1,1],
      [1,0,1,1,1,0,0],
      [1,0,0,0,0,0,0]]

currentpos=[0,1]
endpos=[6,6]

setorder={"N":(lambda x: ([x[0]-1,x[1]],"S"),lambda x: True if x[0]>0 and maze[currentpos[0]-1][currentpos[1]]==0 else False),
          "E":(lambda x: ([x[0],x[1]+1],"W"),lambda x: True if x[1]<len(maze[0])-1 and maze[currentpos[0]][currentpos[1]+1]==0 else False),
          "S":(lambda x: ([x[0]+1,x[1]],"N"),lambda x: True if x[0]<len(maze)-1 and maze[currentpos[0]+1][currentpos[1]]==0 else False),
          "W":(lambda x: ([x[0],x[1]-1],"E"),lambda x: True if x[1]>0 and maze[currentpos[0]][currentpos[1]-1]==0 else False)}

pathstaken={}
previous="N"

pathstaken[str(currentpos)]=[currentpos,[setorder[i][0] for i in setorder if setorder[i][1](currentpos) is True and not previous==i]]
while not currentpos==endpos:
    if len(pathstaken[list(pathstaken.keys())[-1]][1]) > 0:
        currentpos,previous=pathstaken[str(currentpos)][1][0](currentpos)
        pathstaken[list(pathstaken.keys())[-1]][1].pop(0)
        pathstaken[str(currentpos)]=[currentpos,[setorder[i][0] for i in setorder if setorder[i][1](currentpos) is True and not previous==i]]
    else:
        pathstaken.pop(list(pathstaken.keys())[-1])
        currentpos=pathstaken[list(pathstaken.keys())[-1]][0]
        
list(map(print,pathstaken))